from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from twilio.rest import Client
# Create your models here.
import random


class pay(models.Model):
    investor_name = models.CharField(max_length=100)
    mobile_account_number = models.CharField(max_length=15)
    idea_name = models.CharField(max_length=500)
    price = models.FloatField(blank = True)
   
    
    def save(self, *args, **kwargs):

        pr = IdeaPost.objects.all().filter(title = self.idea_name)

        for i in pr:
            print(i.price)
            if self.price == i.price:  
                number = self.mobile_account_number
                code = i.download
                # Your Account SID from twilio.com/console
                account_sid = "ACd2b8a7e0e8af66f8f6208a28553abead"
                # Your Auth Token from twilio.com/console
                auth_token  = "411a39efe05ef0b1041f6c0fe585e03b"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    to= number, 
                    from_="+12017204103",
                    body=code)



            
        return super().save(*args, **kwargs)



class IdeaCategory(models.Model):
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class IdeaPost(models.Model):

    idea = models.ForeignKey(IdeaCategory,on_delete=models.CASCADE,related_name='ideas')

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    title   = models.CharField(max_length=250,unique=True)
    summary = models.TextField(max_length = 10000, blank = False)
    details = models.TextField(max_length = 2000,  blank = False)

    post_image1 = models.ImageField(upload_to="media",verbose_name="Image1", blank=True, null=True)
    post_image2 = models.ImageField(upload_to="media",verbose_name="Image2", blank=True, null=True)
    post_image3 = models.ImageField(upload_to="media",verbose_name="Image3", blank=True, null=True)

    slug = models.SlugField(null=True, blank=True)

    video = models.FileField(upload_to="media",verbose_name="ShortVideo", blank=True, null=True)

    full_video = models.FileField(upload_to="media",verbose_name="FullVideo", blank=True, null=True)

    File = models.FileField(upload_to="media",verbose_name="Upload Zip", blank=True)

    price = models.FloatField(blank=False)

    download = models.IntegerField(blank=True)

    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        self.download = random.randrange(0000,9999) 
        self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return reverse("idea_detail", kwargs={"category": self.idea.slug,"slug":self.slug})
    


class Message(models.Model):
    idea_name = models.ForeignKey(IdeaPost,null=True, on_delete=models.CASCADE,related_name='messages')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    

    