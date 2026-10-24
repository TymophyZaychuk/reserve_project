from django.shortcuts import render
from booking_app.models import *
# Create your views here.
def home(request):
    hotels = Hotel.objects.all()
    return render(request,'home.html',{'hotels':hotels})

def hotel_page(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    return render(request, 'hotel_page.html', {'hotel': hotel})

def review(request):
    if request.method == 'POST':
        user = request.user
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review = Review(user=user, rating=rating, comment=comment)
        review.save()

        return render(request, 'review.html', {'success': True})

    return render(request, 'review.html')