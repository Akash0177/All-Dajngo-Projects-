from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    s='<h1>Hyderabad Jobs Infomation.....!!!!!</h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s='<h1>Pune Jobs Infomation</h1>'
    return HttpResponse(s)

def mumbaijobsinfo(request):
    s='<h1>Mumbai Jobs Infomation</h1>'
    return HttpResponse(s)

def dehlijobsinfo(request):
    s='<h1>Dehli Jobs Infomation</h1>'
    return HttpResponse(s)
