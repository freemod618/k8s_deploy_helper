import os,sys
out=os.popen("kubeadm config images list").read()
print("-"*40)
out_list=out.split("\n")
print(out_list)
out_list.remove("")
def linux_cmd(_in):
    print(_in)
    _out = os.popen(_in).read()
    print(_out)

for i in out_list:
    print("-"*40)
    ali_image_name="registry.cn-hangzhou.aliyuncs.com/google_containers/"+i.split("/")[1]

    pull_image_str="docker pull "+ali_image_name
    linux_cmd(pull_image_str)

    tag_image_str = "docker tag "+ali_image_name+" k8s.gcr.io/"+i.split("/")[1]
    linux_cmd(tag_image_str)

    rm_image_str = "docker rmi "+ali_image_name
    linux_cmd(rm_image_str)
