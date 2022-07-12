from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello1_msg(request):
    return HttpResponse("Linux Says Hello from hello1")