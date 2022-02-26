import os
from django.db import models
from django.contrib.auth.models import User
import phone_field
from phone_field import PhoneField


# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to= "media", verbose_name="Profile Picture", blank=True ,null = True)
    facebooklink = models.CharField(max_length=200,blank=True,null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    enterpreneur = 'enterpreneur'
    investor = 'investor'
    
    user_types = [(enterpreneur,'enterpreneur'),(investor,'investor'),]
    user_type = models.CharField(max_length=50, choices=user_types, default=enterpreneur)

    def __str__(self):
        return self.user.username
