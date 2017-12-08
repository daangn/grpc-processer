import time
import logging
import sys
import signal
from subprocess import Popen, PIPE
from concurrent import futures

import grpc
import click

import processer_pb2 as pb2
import processer_pb2_grpc as pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Processer(pb2_grpc.ProcesserServicer):

    def __init__(self, cmds, header_lines_count=0):
        self._cmds = None
        self._proc = None
        self._header_lines_count = None
        self._load_process(cmds, header_lines_count)

    def Input(self, request, context): 
        logging.debug('input: %s', request.input)

        self._proc.stdin.write("%s\n" % request.input)
        results = []
        for i in range(request.outputs_count or 1):
            line = self._proc.stdout.readline()
            results.append(line[0:-1]) # except newline character

        results = "\n".join(results)
        logging.debug('output: %s', results)
        return pb2.OutputResponse(results=results)

    def Reload(self, request, context): 
        logging.debug('reloading: %s' % request.cmds)
        self._load_process(request.cmds, request.header_lines_count)
        return pb2.Response(message='Reloaded: %s' % (' '.join(self._cmds)))

    def _load_process(self, cmds=None, header_lines_count=None):
        if not cmds:
            cmds = self._cmds
            header_lines_count = self._header_lines_count
        else:
            self._cmds = cmds
            self._header_lines_count = header_lines_count

        pre_proc = self._proc
        self._proc = Popen(cmds,
                stdout=PIPE, stdin=PIPE, bufsize=1, universal_newlines=True)
        logging.info('process loaded: %s' % ' '.join(cmds))

        logging.info('skip header lines count: %d' % header_lines_count)
        for i in range(header_lines_count):
            line = self._proc.stdout.readline()
            logging.info(line[0:-1])

        if pre_proc:
            pre_proc.kill()
            logging.info('pre process killed')

    def stop(self):
        if self.proc:
            self.proc.kill()


@click.command()
@click.option('--log', default='log/processer.log', help='log filepath')
@click.option('--debug', is_flag=True, help='debug')
@click.option('--header_lines_count', default=0, help='skip header lines count')
@click.argument('cmds', nargs=-1)
def serve(cmds, log, debug, header_lines_count):
    if log:
        handler = logging.FileHandler(filename=log)
    else:
        handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s - %(message)s')
    handler.setFormatter(formatter)
    root = logging.getLogger()
    level = debug and logging.DEBUG or logging.INFO
    root.setLevel(level)
    root.addHandler(handler)

    logging.info('server loading...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    servicer = Processer(list(cmds), header_lines_count)
    pb2_grpc.add_ProcesserServicer_to_server(servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info('server started')

    # for docker heath check
    with open('/tmp/status', 'w') as f:
        f.write('started')

    def stop_serve(signum, frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGINT, stop_serve)
    signal.signal(signal.SIGTERM, stop_serve)

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        servicer.stop()
        logging.info('server stopped')

if __name__ == '__main__':
    serve()
