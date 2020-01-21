from django import forms
from .models import Video
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class VideoModelForm(forms.ModelForm):
    
    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0 or rate > 10:
            raise forms.ValidationError('The rate has to be between 0 and 10 !')

        return rate
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise forms.ValidationError('The title is too long !')

        return title
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 1000:
            raise forms.ValidationError('The description is too long !')
        elif len(description) < 10:
            raise forms.ValidationError('The description is too short !')

        return description

    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title','class':'form-control'}),
            'file': forms.FileInput(attrs={'placeholder': 'Image','class':'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description','class':'form-control'}),
            'rate': forms.NumberInput(attrs={'placeholder': 'Rate','class':'form-control'}),
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
