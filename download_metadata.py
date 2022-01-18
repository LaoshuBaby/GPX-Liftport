# Download Metadata: GET /api/0.6/gpx/#id/details
import requests

URL_PATTERN={
    "download_metadata":"https://{server}.openstreetmap.org/api/0.6/gpx/{id}/details",
}

header={
    "Authorization":"Basic {auth}",
}

username="喵耳引力波"
password="0"

def call_func(server_name:str,gpx_id:int,mode:str):
    print("server_name="+server_name,"gpx_id="+str(gpx_id))
    url=URL_PATTERN["download_metadata"].format(server=server_name)
    url=url.format(id=gpx_id)
    if mode=="simple":
        body = requests.get(url)
    else:
        body = requests.get(url,auth=(username,password)) #不愧是你啊，Copilot，我还打算手写header替换和base64库引入来着
    print(body.text)

def init():
    gpx_id=int(input("请输入您想下载的GPX的ID："))
    mode=input("请输入您想工作于哪个服务器：")
    if mode.lower()=="prod" or mode.lower()=="production":
        server_name="www"
    else:
        server_name="master.apis.dev" # "api06.dev"
    # username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    call_func(server_name,gpx_id,"auth")

init()