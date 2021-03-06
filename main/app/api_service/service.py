import inspect
import json
import sys
import urllib
from django.http import HttpResponse
from urllib.parse import urlencode
from urllib.request import urlopen, Request, HTTPSHandler
import ssl
from .exceptions import Error

# from main.settings import cert, key, url, headers
# для отладки
cert = 'client03test.crt'
key = 'client03test.key'
url = "https://slb.medv.ru/api/v2/"
headers = {'content-type': 'application/json'}
values = {"method": "auth.check", "params": [], "jsonrpc": "2.0", "id": 1}


class Service:
    """Базовый класс - обработка ошибок, обработка методов, формат вывода"""

    def get_method(self, method):
        pass

    def service_request(self, request):

        data = json.dumps(values).encode('utf-8')
        context = ssl.create_default_context()
        context.load_cert_chain(certfile=cert, keyfile=key)
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
        response = opener.open(Request(url=url, data=data, headers=headers, ))
        print(response.read().decode())
        if response.getcode() == 200:
            return request
        else:
            return 'ошибка'  # 404 ошибка и тд








# -------- декоратор для работы с JSON-RPC-1-----------
"""
https://github.com/benwilber/jsonrpc/blob/master/jsonrpc.py
"""
#
# class ServiceBase(object):
#
#     def __init__(self, auth_func=None, show_exceptions=False):
#         self.methods = {}
#         self.auth_func = auth_func
#         self.show_exceptions = show_exceptions
#
#     def to_json(self, data):
#         return json.dumps(data)
#
#     def get_response(self, id, result):
#         return {
#             'version': '2.0',
#             'id': id,
#             'result': result,
#             'error': None,
#         }
#
#     def get_error(self, id, code, message):
#         return {
#             'id': id,
#             'version': '2.0',
#             'error': {
#                 'name': 'Error',
#                 'code': code,
#                 'message': message,
#             },
#         }
#
#     def add_method(self, method_name, method):
#         self.methods[method_name] = method
#
#     def is_authorized(self, request, method_name, params):
#
#         if self.auth_func:
#             auth = self.auth_func(request, method_name, params)
#
#             try:
#                 auth, msg = auth
#             except (ValueError, TypeError):
#                 msg = 'method "%s" does not exist' % method_name
#
#             return auth, msg
#
#         return True, ''
#
#     def process_request(self, request):
#         try:
#
#             data = json.loads(request.raw_post_data)
#             id, method_name, params = data['id'], data['method'], data['params']
#         except:
#             # Doing a blanket except here
#             error = self.get_error(id, 100, 'Malformed JSON-RPC 1.1 request')
#             return self.to_json(error)
#
#         auth, auth_msg = self.is_authorized(request, method_name, params)
#         if not auth:
#             error = self.get_error(id, 100, auth_msg)
#             return self.to_json(error)
#
#         method = self.get_method(method_name)
#         if not method:
#             error = self.get_error(id, 100, 'method "%s" does not exist' % method_name)
#             return self.to_json(error)
#
#         try:
#             result = method(request, *params)
#             response = self.get_response(id, result)
#
#         except Exception:
#             if self.show_exceptions:
#                 etype, evalue, etb = sys.exc_info()
#                 response = self.get_error(id, 100, '%s: %s' % (etype.__name__, evalue))
#             else:
#                 response = self.get_error(id, 100, 'An error occurred')
#
#         return self.to_json(response)
#
#     def list_methods(self):
#         return self.methods.keys()
#
#     def get_method(self, method_name):
#         try:
#             return self.methods[method_name]
#         except KeyError:
#             return None
#
#     def get_smd(self, url):
#         smd = {
#             'serviceType': 'JSON-RPC',
#             'serviceURL': url,
#             'methods': []
#         }
#
#         for method_name in self.list_methods():
#             sig = inspect.getfullargspec(self.get_method(method_name))
#             smd['methods'].append({
#                 'name': method_name,
#                 'parameters': [{'name': val} for val in sig.args if \
#                                val not in ('self', 'request')]
#             })
#
#         return self.to_json(smd)
#
#
# class Service(ServiceBase):
#
#     def __call__(self, request):
#         # JSON-RPC method calls come in as POSTs
#         if request.method == 'POST':
#             return HttpResponse(self.process_request(request), mimetype='application/json')
#
#         url = request.get_full_path()
#         return HttpResponse(self.get_smd(url), mimetype='application/json')
#
#
# # декоратор для Service
# def servicemethod(service, name=None):
#     def wrapped(method):
#         if isinstance(service, Service):
#             service.add_method(name or method.__name__, method)
#         else:
#             emsg = 'Service "%s" not found' % service.__name__
#             raise NotImplementedError(emsg)
#         return method
#
#     return wrapped
#
#
# class ServiceProxy(object):
#
#     def __init__(self, url):
#         self.smd_url = url
#         self.service_url = url
#         self.smd = {}
#         self.methods = []
#         self.call_id = 0
#
#     def to_json(self, data):
#         return json.dumps(data)
#
#     def from_json(self, data):
#         return json.loads(data)
#
#     def get_smd(self, url=None):
#         data = urllib2.urlopen(url or self.smd_url)
#         self.smd = self.from_json(data.read())
#         data.close()
#         self.methods += [method['name'] for method in self.smd['methods']]
#
#     def call_method(self, method_name, params):
#         self.call_id += 1
#         data = {
#             'method': method_name,
#             'params': params,
#             'id': self.call_id,
#         }
#         print(data)
#         data = urllib2.urlopen(self.service_url, self.to_json(data))
#         resp = self.from_json(data.read())
#         data.close()
#         return resp
#
#     def __getattr__(self, attr):
#
#         if not self.smd:
#             self.get_smd()
#
#         def wrapped(*args):
#             resp = self.call_method(attr, args)
#             try:
#                 return resp['result']
#             except KeyError:
#                 err_name, err_msg = resp['error']['name'], resp['error']['message']
#                 raise Error('%s: %s' % (err_name, err_msg))
#
#         return wrapped
#
#
# # декоратор для ServiceProxy
# def proxymethod(serviceproxy, name=None):
#     def wrapped(method):
#         def wrapped2(*args):
#             result = getattr(serviceproxy, name or method.__name__)(*args)
#             return method(result)
#
#         return wrapped2
#
#     return wrapped
