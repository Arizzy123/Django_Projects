from django.http import HttpResponse
from django.shortcuts import render

def renderTemplates(request):
    return render(request, 'welcome.html')
# import datetime

# # def home(request):
# #     return HttpResponse("hello world?")

def display(request):
    return HttpResponse('My first Django work')

# def displaydatetime(request):
#     dt=datetime.datetime.now()
#     s="<b>Current date and time: </>" +str(dt)
#     return HttpResponse(s)

# def home(request):
#     return HttpResponse('how are you')


# from django.http import HttpResponse

# def welcome(response):
#     return HttpResponse('How are you doing?')

from django.shortcuts import render

def renderTemplates(request):
    return render(request, 'welcome.html')