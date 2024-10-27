from django.http import HttpResponse
from django.shortcuts import render

from travello.models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mogadishu'
    dest1.desc = 'Mogadishu - Nulla pretium tincidunt felis, nec.'
    dest1.price = 789.8 
    dest1.img = 'destination_7.jpg'
    dest2 = Destination()
    dest2.name = 'San Francisco'
    dest2.desc = 'San Francisco - Nulla pretium tincidunt felis, nec.'
    dest2.price = 600
    dest2.img = 'destination_8.jpg'
    dest3 = Destination()
    dest3.name = 'Beijing'
    dest3.desc = 'Beijing - Nulla pretium tincidunt felis, nec.'
    dest3.price = 500
    dest3.img = 'destination_9.jpg'
    dests = [dest1,dest2, dest3]
    return render(request, 'index.html', {'dests': dests})