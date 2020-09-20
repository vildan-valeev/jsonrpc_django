from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from main.settings import cert, key

from main.app.auth import auth
from .api_service.service import Service

s = Service


@s.service_request()
def main(request, *args, **kwargs):
    return HttpResponse(f'<h1>Авторизация пройдена, Добро пожаловать</h1>')
