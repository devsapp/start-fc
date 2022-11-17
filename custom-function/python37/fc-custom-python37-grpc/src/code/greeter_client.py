"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
import random
import argparse

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import helloworld_resources

parser = argparse.ArgumentParser(description="grpc params")
parser.add_argument('--name', '-name', help='name ', default='world')
parser.add_argument('--addr', '-addr', help="addr to connect ", default='localhost')
args = parser.parse_args()


def make_route_note(message, latitude, longitude):
    return helloworld_pb2.RouteNote(
        message=message,
        location=helloworld_pb2.Point(latitude=latitude, longitude=longitude))


def greeting_hello(stub):
    response = stub.SayHello(helloworld_pb2.HelloRequest(name=args.name))
    print("Greeter client received: " + response.message)


def helloworld_list_features(stub):
    rectangle = helloworld_pb2.Rectangle(
        lo=helloworld_pb2.Point(latitude=400000000, longitude=-750000000),
        hi=helloworld_pb2.Point(latitude=420000000, longitude=-730000000))
    print("Looking for features between 40, -75 and 42, -73")

    features = stub.ListFeatures(rectangle)

    for feature in features:
        print("Feature called %s at %s" % (feature.name, feature.location))


def generate_route(feature_list):
    for _ in range(0, 10):
        random_feature = feature_list[random.randint(0, len(feature_list) - 1)]
        print("Visiting point %s" % random_feature.location)
        yield random_feature.location


def helloworld_record_route(stub):
    feature_list = helloworld_resources.read_route_guide_database()

    route_iterator = generate_route(feature_list)
    route_summary = stub.RecordRoute(route_iterator)
    print("Finished trip with %s points " % route_summary.point_count)
    print("Passed %s features " % route_summary.feature_count)
    print("Travelled %s meters " % route_summary.distance)
    print("It took %s seconds " % route_summary.elapsed_time)


def generate_messages():
    messages = [
        make_route_note("First message", 0, 0),
        make_route_note("Second message", 0, 1),
        make_route_note("Third message", 1, 0),
        make_route_note("Fourth message", 0, 0),
        make_route_note("Fifth message", 1, 0),
    ]
    for msg in messages:
        print("Sending %s at %s" % (msg.message, msg.location))
        yield msg


def helloworld_route_chat(stub):
    responses = stub.RouteChat(generate_messages())
    for response in responses:
        print("Received message %s at %s" %
              (response.message, response.location))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    # Digicert-OV-DV-root.cert 为对应ssl证书类型的根证书，与server端证书不同
    ca_cert = open("../Digicert-OV-DV-root.cer", 'rb').read()
    credentials = grpc.ssl_channel_credentials(ca_cert)
    with grpc.secure_channel(args.addr + ':8089', credentials) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        print("-------------- Greeting Say Hello----------------")
        greeting_hello(stub)
        # print("-------------- ListFeatures --------------")
        # helloworld_list_features(stub)
        # print("-------------- RecordRoute --------------")
        # helloworld_record_route(stub)
        # print("-------------- RouteChat --------------")
        # helloworld_route_chat(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
