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
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from . import views
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# 사용자 호출 -> View.as_view() -> dispatch() 다음 호출이 분기
# GET요청 : dispatch() -> get()
# POST요청: dispatch() -> post()

app_name = 'account'

urlpatterns = [
    # path('join', views.UserCreateView.as_view(), name="join"), #가입
    path('join', CreateView.as_view(template_name="account/join_form.html", 
                                    form_class=CustomUserCreationForm,
                                    success_url = reverse_lazy('home')), 
                                    name='join'),
    # path('login', views.UserLoginView.as_view(), name='login'), # 로그인
    path('login', LoginView.as_view(template_name='account/login_form.html', 
                                    form_class=AuthenticationForm), 
                                    name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
]