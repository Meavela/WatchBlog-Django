from django import forms
from .models import Video
from django.contrib.auth.models import User

class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
