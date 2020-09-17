import json
from urllib import request
import requests
from urllib.parse import urlencode
from urllib.request import urlopen, Request, URLopener

cert = 'client03test.crt'
key = 'client03test.key'
url = "https://slb.medv.ru/api/v2/"
headers = {
    'content-type': 'application/json',
}
values = {
    "method": "auth.check",
    "params": [],
    "jsonrpc": "2.0",
    "id": 1,
}


def main():
    response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(values))
    print(response.json())


def main2():
    data = urlencode(values).encode()
    URLopener(key_file=key, cert_file=cert)
    # TODO: вписать URLopener в запрос, передать сертификаты в **x509
    response = urlopen(Request(url=url, data=data, headers=headers, ), timeout=60).read().decode()
    print(response)


if __name__ == "__main__":
    # main()
    main2()
