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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views


# 사용자 호출 -> View.as_view() -> dispatch() 다음 호출이 분기
# GET요청 : dispatch() -> get()
# POST요청: dispatch() -> post()

app_name = 'board'

urlpatterns = [
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),# 계시물 상세 페이지.
    path('create', views.PostCreateView.as_view(), name="create"), # 글 등록 View url
    path('update/<int:pk>', views.PostUpdateView.as_view(), name="update"), 
    # update: 글 수정처리 url. GET: 수정할 게시물의 pk를 path parameter로 받아야함.
    path('delete/<int:pk>', views.post_delete, name='delete'), # 삭제 처리.
    path('list', views.PostListView.as_view(), name="list"),
]
