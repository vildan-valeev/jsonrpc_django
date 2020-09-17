import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# from ..main.settings import key, cert
import json
from django.http import request
from django.views.decorators.csrf import csrf_protect
import urllib
from main.settings import cert, key


# def auth(request):
#     url = "https://slb.medv.ru/api/v2/"
#     headers = {
#         'content-type': 'application/json',
#     }
#     payload = {
#         "method": "auth.check",
#         "params": [],
#         "jsonrpc": "2.0",
#         "id": 1,
#     }
#     # HttpRequest.POST
#     response = requests.post(url, cert=(cert, key), verify=False, headers=headers, data=json.dumps(payload))
#     print(response.json())
#     # return HttpResponse(f'<h3>{response.json()}</h3>')
#     return JsonResponse(response.json())



def auth(request):
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
    # HttpRequest.POST
    response = requests.post(url, cert=(cert, key), verify=False, headers=headers, data=json.dumps(payload))
    print(response.json())
    # return HttpResponse(f'<h3>{response.json()}</h3>')
    return JsonResponse(response.json())