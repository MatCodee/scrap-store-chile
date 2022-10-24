import requests

def api_request(url):
    r = requests.get(url)
    return r.content