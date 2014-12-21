import requests
import json


def make_post_request(url="http://127.0.0.1:80", data={}):
    r = requests.post(url, data=json.dumps(data))
    content = r.text

    return content

print(make_post_request("http://127.0.0.1:5000"))