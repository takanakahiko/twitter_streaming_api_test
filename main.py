import requests
from requests_oauthlib import OAuth1
import json
import urllib

f = open('keys.json', 'r')
keys = json.load(f)

api_key = keys["api_key"]
api_secret = keys["api_secret"]
access_token = keys["access_token"]
access_secret = keys["access_secret"]

url = "https://userstream.twitter.com/1.1/user.json"

auth = OAuth1(api_key, api_secret, access_token, access_secret)

r = requests.post(url, auth=auth, stream=True, data={"track":"emacs"})

for line in r.iter_lines():
    print line
    if line != "":
        data = json.loads(line)
        if "text" in data:
            print urllib.unquote(data["text"])