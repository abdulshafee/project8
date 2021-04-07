from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>welcome to bemalkheda</h1>")

def base(request):
        return render(request,"sample.html")

def demo2(request):
        return render(request,"pro/demo2.html")