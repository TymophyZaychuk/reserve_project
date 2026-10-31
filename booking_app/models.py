from django.db import models
from django.conf import settings

# Create your models here.
class Hotel(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]


    hotel_name = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=200)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='standard')
    rooms = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    def __str__(self):
        return self.hotel_name

    
class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    rooms = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)

    def __str__(self):
        return f"{self.hotel.hotel_name} - {self.room_type}"

    
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reservation_start_date = models.DateField()
    reservation_end_date = models.DateField()
    rooms_booked = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.room}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"

class Meta:
    verbose_name = "Reservation"
    verbose_name_plural = "Reservations"
    ordering = ['reservation_start_date']
