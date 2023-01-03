from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username','email','password1','password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio','address']
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name','username']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }