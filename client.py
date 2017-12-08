from __future__ import print_function

import grpc
import click

import processer_pb2 as pb2
import processer_pb2_grpc as pb2_grpc


@click.command()
@click.option('--port', default=50051, help='docker port')
@click.option('--input', help='input')
@click.option('--outputs_count', type=int, help='outputs_count')
@click.argument('action')
def run(action, port, input, outputs_count):
    channel = grpc.insecure_channel('localhost:%d' % port)
    stub = pb2_grpc.ProcesserStub(channel)

    if action == 'input':
        request = pb2.InputRequest(input=input, outputs_count=outputs_count)
        response = stub.Input(request)
        print("output: %s" % response.results)
    elif action == 'reload':
        request = pb2.ReloadRequest()
        response = stub.Reload(request)
        print(response.message)
        assert response.message.startswith('Reloaded: ')
    else:
        print('Invalid action: %s' % action)

if __name__ == '__main__':
  run()
