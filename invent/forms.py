from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    
class Meta:
    model = User
    fields = ['id','username', 'email','password1', 'password2']

        
    
