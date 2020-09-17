import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# from ..main.settings import key, cert
import json
from django.http import request
from django.views.decorators.csrf import csrf_protect

from main.settings import cert, key

# @csrf_protect
def auth(request):

    url = "https://slb.medv.ru/api/v2/"
    headers = {
        'content-type': 'application/json',
    }
    payload = {
        "method": "test",
        "params": [],
        "jsonrpc": "2.0",
        "id": 1,
    }
    HttpRequest.POST
    response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(payload))
    print(response.json())
    # return HttpResponse(f'<h3>{response.json()}</h3>')
    return JsonResponse(response.json())
