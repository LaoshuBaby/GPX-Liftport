# Download Metadata: GET /api/0.6/gpx/#id/details
import requests

URL_PATTERN={
    "download_metadata":"https://{server}.openstreetmap.org/api/0.6/gpx/{id}/details",
}

def call_func(server_name:str,gpx_id:int):
    print("server_name="+server_name,"gpx_id="+str(gpx_id))
    url=URL_PATTERN["download_metadata"].format(server=server_name)
    url=url.format(id=gpx_id)
    body = requests.get(url)
    print(body.text)

def init():
    gpx_id=int(input("请输入您想下载的GPX的ID："))
    mode=input("请输入您想工作于哪个服务器：")
    if mode.lower()=="prod" or mode.lower()=="production":
        server_name="www"
    else:
        server_name="master.apis.dev" # "api06.dev"
    call_func(server_name,gpx_id)

init()