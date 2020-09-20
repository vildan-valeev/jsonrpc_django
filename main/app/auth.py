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






method_response = {'method': 'auth.check', 'code_response': 200}

def decorator_function(method):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(*args, **kwargs)
            print('Выполняем обёрнутую функцию...')
            func(*args, **kwargs)
            print('Выходим из обёртки')

        return wrapper
    if method == method_response['method']:
        print(f'ок: this method  is {method}')
        return actual_decorator
    else:
        print("Неправильный метод")

@decorator_function(method='auth.chec')
def main(request):
    txt = "Отлично, доступ получен"
    print(f'{txt}: {request}')
