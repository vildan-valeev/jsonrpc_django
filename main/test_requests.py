import json

import requests

# from requests import Request, Session
CERTIFICATE = 'a66350f1167b506880cead974cec485ff64e94090b7c1900105f136872e3801f'
KEY = 'edf27f8cc7553d8c7ed5883f81ab4318c817618a16d9eef1145e198ffcfd26c0'

cert = 'client03test.crt'
key = 'client03test.key'
url = "https://slb.medv.ru/api/v2/"


def main():
    url = "https://slb.medv.ru/api/v2/"
    headers = {
        'content-type': 'application/json',
    }
    payload = {
        "method": "auth.check",
        "params": [],
        "jsonrpc": "2.0",
        "id": 1,
    }

    # response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(payload))
    response = requests.post(url, cert=(CERTIFICATE, KEY), verify=True, headers=headers, data=json.dumps(payload))
    print(response.json())


if __name__ == "__main__":
    main()
