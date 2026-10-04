from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

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

    
class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    reservation_start_date = models.DateField()
    reservation_end_date = models.DateField()
    rooms_booked = models.IntegerField()

    def __str__(self):
        return f"{self.guest.name} - {self.hotel.hotel_name}"

class Meta:
    verbose_name = "Reservation"
    verbose_name_plural = "Reservations"
    ordering = ['reservation_start_date']