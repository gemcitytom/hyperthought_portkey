from django.shortcuts import render

from django.http import HttpResponse


def basic_ayasdi_apps(request):
    return render(request,"bao/basic_ayasdi_apps.html")

# Create your views here.
