from __future__ import print_function

import cProfile
import logging
import time

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        start_time = time.time()
        response = stub.SayHello(helloworld_pb2.HelloRequest(Name_Name="you"))
    print(f"need time {time.time() - start_time}")
    # print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    # cProfile.run("run()")
    run()
