from django import forms
from django.forms import fields, widgets
from .models import event


class PostForm(forms.ModelForm):

    class Meta:
        model = event
        fields = ('title','details', 'event_poster', 'numberofpeople','company','contact_details','online_link')
        widgets = {

                        'title': forms.TextInput(attrs={'class': 'form-control'}),
                        'details': forms.Textarea(attrs={'class': 'form-control'}),
                        'numberofpeople': forms.TextInput(attrs={'class': 'form-control'}),
                        'company': forms.TextInput(attrs={'class': 'form-control'}),
                        'contact_details': forms.Textarea(attrs={'class': 'form-control'}),
                        'online_input': forms.TextInput(attrs={'class': 'form-control'}),

        } 
 

