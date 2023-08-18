from django.conf import settings
from django.shortcuts import render
# chatbotapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai

from chatbotapp.models import Conversation

openai.api_key = settings.OPENAI_API_KEY


from django.shortcuts import render
from django.http import JsonResponse
import openai

def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        chat_history = request.POST.get("chat_history", "")

        # ChatGPT 모델로부터 예측된 대화 내용을 받아오는 함수
        def generate_response(prompt):

            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=50
            )

            return response.choices[0].text.strip()

        bot_response = generate_response(f"{chat_history}\nUser: {user_input}")
        conversation = Conversation(user_input=user_input, content=bot_response)
        conversation.save()

        return JsonResponse({"bot_response": bot_response, "chat_history": chat_history})

    return render(request, "chatbotapp/chat.html")

