from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "user/login.html")


def join(request):
    return render(request, "user/join.html")