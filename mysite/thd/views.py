from django.shortcuts import render

from django.http import HttpResponse


def thd_apps(request):
    return render(request,"thd/thd_apps.html")

# Create your views here.
