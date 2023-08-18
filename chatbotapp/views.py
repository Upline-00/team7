from django.shortcuts import render
# chatbotapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"


def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        chat_history = request.POST.get("chat_history", "")

        prompt = f"{chat_history}User: {user_input}\nChatGPT:"
        bot_response = generate_response(prompt)

        # 대화 내용 저장 (실제로는 데이터베이스에 저장하는 코드로 변경 필요)
        save_conversation(user_input, bot_response)

        return JsonResponse({"bot_response": bot_response})

    return render(request, "chatbotapp/chat.html")  # chat.html 템플릿 생성 필요
