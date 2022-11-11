from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def main(request):
    return render(request, "index.html")
    
def hello(request):
    if request.method == "GET":
        return HttpResponse("hello")

def goodby(request):
    if request.method == "GET":
        return HttpResponse("goodby user!")

def now_date(request):
    if request.method == "GET":
        return HttpResponse(date.today())
