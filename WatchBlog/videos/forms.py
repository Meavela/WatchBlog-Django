from django import forms
from .models import Video
from django.contrib.auth.models import User

class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title','class':'form-control'}),
            'file': forms.FileInput(attrs={'placeholder': 'Image','class':'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description','class':'form-control'}),
            'rate': forms.TextInput(attrs={'placeholder': 'Rate','class':'form-control'}),
            'date': forms.DateInput(attrs={'placeholder': 'Date','class':'form-control', 'type':'date'}),
            'type_video': forms.Select(attrs={'placeholder': 'Type','class':'form-control'}),
            'category_video': forms.Select(attrs={'placeholder': 'Category','class':'form-control'}),
            'user': forms.Select(attrs={'placeholder': 'User','class':'form-control'}),
        }

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
