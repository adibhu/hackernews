from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1']


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

def signup(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')

    else:
        form =  UserRegisterForm()

    return render(request, 'core/signup.html',{'form':form})
