from django.shortcuts import render

from django.http import HttpResponse


def adv_ayasdi_apps(request):
    return render(request,"aao/adv_ayasdi_apps.html")
# Create your views here.
