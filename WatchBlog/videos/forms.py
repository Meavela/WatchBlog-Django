from django import forms
from .models import Video
from django.contrib.auth.models import User

class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
