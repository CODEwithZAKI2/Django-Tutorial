from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sayHello(request):
    return render(request=request, template_name='hello.html', context= {'django': 'Django'})