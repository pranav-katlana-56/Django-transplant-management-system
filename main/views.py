from django.http.response import HttpResponse
from django.shortcuts import render
import template

def main(request):
    return render(request, 'home.html')