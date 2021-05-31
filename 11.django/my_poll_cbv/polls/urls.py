"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py url - view연결
# polls/urls.py -> polls app용 url pattern 설정 스크립트.

from django.urls import path
from . import views
from .models import Question
from django.views.generic import ListView, DetailView
# 이 url pattern들의 namespace(prefix)로 사용할 값 설정.
# urlpattern 설정의 이름 호출시 다른app들과 구분하기 위해 사용한다.
app_name = "polls"

urlpatterns = [
    # CBV글 등록 : ViewClass이름.as_view()
    # path('list', views.list, name='list'),
    # path('list', views.QuestionListView.as_view(), name='list'),
    path('list', ListView.as_view(model=Question,template_name="polls/list.html"), name='list'),
    # path('vote_form/<int:question_id>', views.vote_form, name='vote_form'),
    path('vote_form/<int:question_id>', views.VoteView.as_view(), name='vote'),
    # path('vote', views.vote, name='vote'),
    # path('vote_result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result'),
    path('vote_result/<int:pk>', DetailView.as_view(model=Question, template_name="polls/vote_result.html"), name='vote_result'),
]