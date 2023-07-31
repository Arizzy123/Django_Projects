from django.shortcuts import render
from django.http import HttpResponse
import datetime


# # Create your views here.

# def displayQuote(request):
#     return HttpResponse ('The best investment you should do is to invest in yourself')

def showtime(request):
    dt=datetime.datetime.now()
    s='<b>The current date and time: </>' +str(dt)
    return HttpResponse(s)

def show(response):
    return HttpResponse('Be yourself')
