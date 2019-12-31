from django.shortcuts import render

from django.http import HttpResponse

#from datetime import date



def index(request):
    return render(request,"sail/home.html")

# Create your views here.
