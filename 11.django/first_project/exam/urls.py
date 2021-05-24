# exam/urls.py

from django.urls import path
from . import views
urlpatterns = [
    # http://ip:port/exam/hello1 => views.hello1함수를 실행.
    path("hello1", views.hello1, name='hello1'),
    path("hello2", views.hello2, name='hello2'),
]