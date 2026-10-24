from django.contrib import messages
from django.shortcuts import render , redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.fields['email'] = forms.EmailField(required=True, label='Email')
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save(update_fields=['email'])
            auth_login(request, user)
            return redirect('home')    
        
    else:
        form = UserCreationForm()
        form.fields['email'] = forms.EmailField(required=True, label='Email')
        messages.error(request, 'error')

    return render(
        request,
        template_name='register.html',
        context={
            'form': form
        }
        )

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


def account(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'account.html')
