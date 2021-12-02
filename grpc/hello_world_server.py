"""
tutorial:https://grpc.io/docs/languages/python/quickstart/
生成grpc code：python -m grpc_tools.protoc -I proto_path --python_out=. --grpc_python_out=. proto_path/helloworld.proto
"""
import logging
from concurrent import futures

from google.protobuf.json_format import MessageToDict

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

logger = logging.getLogger(__name__)


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self) -> None:
        super().__init__()

        self.ls_message = ["c" for i in range(10000)]
        self.message = "".join(self.ls_message)

    def SayHello(self, request, context):
        print(request)
        # res = MessageToDict(
        #     message=request.Name_Name, including_default_value_fields=True
        # )
        # print(res)
        # logger.info(f"发送字节数为{len(message.encode())}")
        return helloworld_pb2.HelloReply(
            message="%s, %s!" % (self.message, request.Name_Name)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()
