from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, "articles/home.html")
    return render(request, "articles/index.html")
