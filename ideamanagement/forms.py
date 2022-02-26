from django import forms
from django.db import models
from django.db.models import fields
from .models import IdeaCategory,IdeaPost, Message

class IdeaForm(forms.ModelForm):
    class Meta:
        model = IdeaPost
        fields =  ['title','summary','details','post_image1','post_image2','post_image3','video','full_video','File','price' ]
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        labels = {"body":"Message:"}
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':"Enter Your Meesage"}),
        }