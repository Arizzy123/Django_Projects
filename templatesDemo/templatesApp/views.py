from django.shortcuts import render

from django.http import HttpResponse

def renderTemplate(request):
    my_dict={"name":"Ridwan","id":123,"sal":5000000000}
    return render(request,'welcome.html', context=my_dict)

def renderEmployee(request):
    my_dict={"name":"Ridwan","id":123,"sal":5000000000}
    return render(request, 'employee.html', my_dict)


# # Create your views here.
def renderEmploy(request):
    return render(request, 'employee.html')