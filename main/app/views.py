from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from main.settings import cert, key
from .service import auth


@auth
def main(request, *args, **kwargs):
    return HttpResponse(f'<h1>Авторизация пройдена, Добро пожаловать</h1>')
