from django.db import models

# Create your models here.
# chatbotapp/models.py
from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_input} | Bot: {self.content}"

