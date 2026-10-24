from django.urls import path
from django.contrib.auth.views import LogoutView
from auth_system import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
