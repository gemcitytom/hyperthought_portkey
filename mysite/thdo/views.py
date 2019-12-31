from django.shortcuts import render

from django.http import HttpResponse


def thd_ops(request):
    return render(request,"thdo/thd_ops.html")

# Create your views here.
