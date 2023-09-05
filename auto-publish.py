# coding=utf-8

import os

os.system("s3 registry login --token {}".format(os.environ["REGISTRY_TOKEN"]))


def search_publish_yaml(directory):
    for root, dirs, files in os.walk(directory):
        if "publish.yaml" in files:
            d = os.path.join(os.getcwd(), root)
            print("try publish dir = {}".format(d))
            try:
                os.system("cd {} && s3 registry publish cd -".format(d))
            except Exception as e:
                print(str(e))


# 在当前目录递归搜索
search_publish_yaml(".")
