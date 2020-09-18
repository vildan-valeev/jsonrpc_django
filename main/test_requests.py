import json
import urllib

import requests
from urllib.parse import urlencode
from urllib.request import urlopen, Request, URLopener, HTTPSHandler
import ssl


cert = 'client03test.crt'
key = 'client03test.key'
url = "https://slb.medv.ru/api/v2/"
headers = {'content-type': 'application/json'}
values = {"method": "auth.check", "params": [], "jsonrpc": "2.0", "id": 1}


def main():
    """requests lib"""
    response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(values))
    print(response.json())

def main2():
    """urllib"""
    data = json.dumps(values).encode('utf-8')

    context = ssl.create_default_context()
    context.load_cert_chain(certfile=cert, keyfile=key)
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
    response = opener.open(Request(url=url, data=data, headers=headers, )).read().decode()
    print(response)

    # response = opener.open(Request(url=url, data=data, headers=headers, ))
    # print(response.getcode())


def auth(func):

    def wrapper(*args, **kwargs):
        # if response.getcode() == 200:
        func()
        # else:
        #     return 'ошибка соединения'
    return wrapper


@auth
def action():
    print('ok')




if __name__ == "__main__":
    # main()
    main2()
    # action()
