from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    dest1= Destination()
    dest1.name='Mumbai'
    dest1.image='destination_1.jpg'
    dest1.description='The City that Never Sleeps'
    dest1.price=790
    dest1.offer=False

    dest2= Destination()
    dest2.name='Colombo'
    dest2.image='destination_2.jpg'
    dest2.description='The capital of Sri Lanka'
    dest2.price=990
    dest2.offer=True



    dest3= Destination()
    dest3.name='Galle'
    dest3.image='destination_3.jpg'
    dest3.description='Hey it\'s home'
    dest3.price=890
    dest3.offer=True


    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
