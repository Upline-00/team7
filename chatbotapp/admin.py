from django.contrib import admin

# Register your models here.

# chatbotapp/admin.py
from django.contrib import admin
from .models import Conversation

admin.site.register(Conversation)

