import subprocess
import time

with open('update.list') as f:
    publish_list = [eve_app.strip() for eve_app in f.readlines()]

for eve_app in publish_list:
    times = 1
    while times <= 3:
        print("----------------------: ", eve_app)
        publish_script = 'https://serverless-registry.oss-cn-hangzhou.aliyuncs.com/publish-file/python3/hub-publish.py'
        command = 'cd %s && wget %s && python hub-publish.py' % (eve_app, publish_script)
        child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, )
        stdout, stderr = child.communicate()
        if child.returncode == 0:
            print("stdout:", stdout.decode("utf-8"))
            break
        else:
            print("stdout:", stdout.decode("utf-8"))
            print("stderr:", stderr.decode("utf-8"))
            time.sleep(3)
            if times == 3:
                raise ChildProcessError(stderr)
        times = times + 1
