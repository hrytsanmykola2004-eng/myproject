from django.http import HttpResponse

from django.shortcuts import render

def bye (request):
    return render (request, "bye.html")
