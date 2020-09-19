import json
import ssl
import urllib
from urllib.request import urlopen, Request
from main.settings import cert, key, url, headers

values = {"method": "auth.check", "params": [], "jsonrpc": "2.0", "id": 1}


# --------простой декоратор авторизации-----------
def auth(func):
    data = json.dumps(values).encode('utf-8')
    context = ssl.create_default_context()
    context.load_cert_chain(certfile=cert, keyfile=key)
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
    response = opener.open(Request(url=url, data=data, headers=headers, ))
    print(response.read().decode())
    if response.getcode() == 200:
        return func
    else:
        return 'ошибка'

