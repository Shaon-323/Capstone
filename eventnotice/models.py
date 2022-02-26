from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class event(models.Model):
   
    posted_by = models.ForeignKey(User,on_delete=CASCADE)
    title   = models.CharField( max_length=200,blank=True,null=True)
    details = models.CharField( max_length=500,blank=True,null=True)
    event_poster = models.ImageField(upload_to= "media", verbose_name="Poster", blank=True ,null = True)
    numberofpeople = models.IntegerField(null=True)
    creation = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=100,blank=True,null=True)
    contact_details = models.CharField(max_length=100,blank=True,null=True)
    online_link =  models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    