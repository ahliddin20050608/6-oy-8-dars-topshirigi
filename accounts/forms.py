from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
 
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    phone = forms.CharField(max_length=50, required=False)
    
    
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'password1', 'password2']
    
    
    