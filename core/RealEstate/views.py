from django.shortcuts import render
from django.http import HttpResponse

class HttpResponseOk(HttpResponse):
    status_code = 200