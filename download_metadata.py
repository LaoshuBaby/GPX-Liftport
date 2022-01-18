# Download Metadata: GET /api/0.6/gpx/#id/details
import requests

URL_PATTERN={
    "download_metadata":"https://{server}.openstreetmap.org/api/0.6/gpx/{id}/details",
}

header={
    "Authorization":"Basic {auth}",
}

username="0"
password="0"

def call_func(server:str, id:int, mode:str):
    print("server=" + server,"id=" + str(id))
    url=URL_PATTERN["download_metadata"].format(server=server,id=id)
    print("url=" + url)
    if mode=="simple":
        body = requests.get(url)
    else:
        body = requests.get(url,auth=(username,password))
    print(body.text)

def init():
    gpx_id=int(input("请输入您想下载的GPX的ID："))
    mode=input("请输入您想工作于哪个服务器：")
    if mode.lower()=="prod" or mode.lower()=="production":
        server_name="www"
    else:
        server_name="master.apis.dev" # "api06.dev"
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    call_func(server_name,gpx_id,"auth")

init()