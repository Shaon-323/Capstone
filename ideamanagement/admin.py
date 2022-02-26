from django.contrib import admin
from .models import IdeaCategory, IdeaPost, Message,  pay
# Register your models here.

admin.site.register(IdeaCategory)
admin.site.register(IdeaPost)
admin.site.register(pay)

admin.site.register(Message)


