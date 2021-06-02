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
from django.urls import path, include
from polls import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

app_name = "account"
urlpatterns = [
    # LoginView - GET 요청: template_name의 template로 이동(render())->로그인 입력폼.
    #             POST요청: 요청파라미터로 받은 
    path('login', LoginView.as_view(template_name="account/login_form.html"), name="login"),
    # LogoutView - 로그아웃 처리후에 setting.py의 LOGOUT_REDIRECT_URL의 설정 URL로 이동.
    path('logout', LogoutView.as_view(), name='logout'),
    path('join', CreateView.as_view(template_name="account/join_form.html", 
                                    form_class=UserCreationForm,
                                    # success_url='/account/login'.
                                    success_url=reverse_lazy('account:login')),
                                    name='join'),
]