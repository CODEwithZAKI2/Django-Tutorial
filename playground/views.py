from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sayHello(request):
    return render(request=request, template_name='home.html', context= {'django': 'Django'})

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    total = num1 + num2
    return render(request, 'result.html', {'result': total})