from django.urls import path
from . import views

app_name = 'askapp'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='list'),
    path('write/', views.QuestionCreateView.as_view(), name='write'),
    path('detail/<int:question_pk>/', views.detail_view, name='detail'),
    # 추가적인 URL 패턴을 여기에 추가할 수 있습니다.
]

