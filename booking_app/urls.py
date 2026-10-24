from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('hotel/<int:hotel_id>/', views.hotel_page, name='hotel_page'),
    path('review/', views.review, name='review'),
]
