from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userprofile.models import UserProfileInfo
import phone_field
from phone_field import PhoneField

class UserForm(UserCreationForm):
    
    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')


        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    
    profile_pic = forms.ImageField(required=True)

    enterpreneur = 'enterpreneur'
    investor = 'investor'
    
    user_types = [(enterpreneur,'enterpreneur'),(investor,'investor'),]

    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','facebooklink','phone','user_type',)
