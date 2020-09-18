from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from main.settings import cert, key

from .auth import auth


@auth
def main(request):
    return HttpResponse(f'<h1>Авторизация пройдена, Добро пожаловать</h1>')
