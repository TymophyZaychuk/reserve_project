from django.shortcuts import render
from booking_app.models import *
# Create your views here.
def home(request):
    hotels = Hotel.objects.all()
    return render(request,'home.html',{'hotels':hotels})

def hotel_page(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    return render(request, 'hotel_page.html', {'hotel': hotel})

