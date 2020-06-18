from django import forms

from django.contrib.auth.models import User
from basic_app.models import UserProfileinfo

class UserForms(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

        
class UserProfleForms(forms.ModelForm):
    class Meta():
        model=UserProfileinfo
        fields=('profile_site','profile_pic')


