from django.shortcuts import render , redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.fields['email'] = forms.EmailField(required=True, label='Email')
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save(update_fields=['email'])
            login(request, user)
            return redirect('home')    
        
    else:
        form = UserCreationForm()
        form.fields['email'] = forms.EmailField(required=True, label='Email')

    return render(
        request,
        template_name='register.html',
        context={
            'form': form
        }
        )
