# coding=utf-8

import os
import subprocess

os.system("s registry login --token {}".format(os.environ["REGISTRY_TOKEN"]))


def search_publish_yaml(directory):
    succ_app_list = []
    for root, dirs, files in os.walk(directory):
        if "publish.yaml" in files:
            d = os.path.join(os.getcwd(), root)
            d = d.replace("/./", "/")
            cmd = ["s", "registry", "publish"]
            result = subprocess.run(
                cmd, cwd=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            exit_code = result.returncode
            print("publish {};  =====>   ExitCode={}".format(d, exit_code))

            if exit_code != 0:
                errMsg = ""
                errMsg += result.stdout
                errMsg += result.stderr
                if "当前版本号应当大于前一次版本号" not in errMsg:
                    print(errMsg)
            else:
                succ_app_list.append(d)

    print("\n\npublish success app list:\n")
    for item in succ_app_list:
        print("{} published success".format(item))


# 在当前目录递归搜索
search_publish_yaml(".")
