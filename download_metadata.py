# Download Metadata: GET /api/0.6/gpx/#id/details
import requests

URL_PATTERN={
    "download_metadata":"https://www.openstreetmap.org/api/0.6/gpx/{id}/details",
}

id=int(input())

body=requests.get(URL_PATTERN["download_metadata"].format(id=id))
print(body.text)