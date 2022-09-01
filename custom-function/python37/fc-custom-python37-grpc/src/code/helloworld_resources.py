import json

import helloworld_pb2


def read_route_guide_database():
    """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    feature_list = []
    with open("helloworld_db.json") as helloworld_db_file:
        for item in json.load(helloworld_db_file):
            feature = helloworld_pb2.Feature(
                name=item["name"],
                location=helloworld_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]))
            feature_list.append(feature)
    return feature_list
