from __future__ import print_function

import grpc

import processer_pb2 as pb2
import processer_pb2_grpc as pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = pb2_grpc.ProcesserStub(channel)
  input = ['input text', 'second text']

  request = pb2.InputRequest(input="\n".join(input), outputs_count=len(input))
  response = stub.Input(request)
  print("output: %s" % response.results)
  assert input == response.results

  request = pb2.ReloadRequest(cmds=['cat'])
  response = stub.Reload(request)
  print(response.message)
  assert request.message.startswith('Reloaded: ')

if __name__ == '__main__':
  run()
