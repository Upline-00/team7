from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Question
from django.shortcuts import render

class QuestionListView(ListView):
    model = Question
    template_name = 'askapp/list.html'
    context_object_name = 'questions'
    ordering = ['-created_at']

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'askapp/write.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('askapp:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def detail_view(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    return render(request, 'askapp/detail.html', {'question': question})



