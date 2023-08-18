

from django.urls import path
from . import views

app_name = "chatbotapp"

urlpatterns = [
    path("chat/", views.chat_view, name="chatbot"),
]
