from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        loginform = AuthenticationForm(data=request.POST)
        registrationform = UserRegisterForm(request.POST)

        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('frontpage')

        elif registrationform.is_valid():
            user = registrationform.save()
            login(request, user)

            return redirect('frontpage')

    else:
        loginform = AuthenticationForm()
        registrationform = UserRegisterForm()

    return render(request, 'core/signup.html', {'loginform': loginform, 'registrationform': registrationform})
