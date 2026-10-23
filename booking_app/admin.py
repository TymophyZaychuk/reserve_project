from django.contrib import admin

from booking_app.models import *

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Review)
