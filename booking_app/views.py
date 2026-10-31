import datetime

from django.shortcuts import render
from booking_app.models import *
# Create your views here.
def home(request):
    hotels = Hotel.objects.all()
    return render(request,'home.html',{'hotels':hotels})


def hotel_page(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)

    return render(request, 'hotel_page.html', {
        'hotel': hotel,
        'rooms': rooms,
        'today': datetime.date.today()
    })

def review(request):
    if request.method == 'POST':
        user = request.user
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review = Review(user=user, rating=rating, comment=comment)
        review.save()

        return render(request, 'review.html', {'success': True})

    return render(request, 'review.html')

def room_page(request, room_id):
    room = Room.objects.get(id=room_id)

    return render(request, 'room_page.html', {
        'room': room,
        'today': datetime.date.today()
    })