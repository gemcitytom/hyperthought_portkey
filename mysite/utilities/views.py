from django.shortcuts import render

from django.http import HttpResponse

from utilities.sourcehandler import sourceList


def utility_apps(request):
    listing=sourceList()
    dictList={}
    context={"listing":listing}
    #return render(request,"utilities/utility_apps.html",context)
    return render(request,"utilities/utilities_test.html",context)

# Create your views here.
