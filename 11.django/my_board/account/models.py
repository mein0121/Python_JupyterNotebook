from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# 사용자정의 user모델 -> AbstractUser 확장(상속) : 기존 User모델 + 추가 Field
class CustomUser(AbstractUser):
    # Model Field 작성 => 추가 User Field
    GENDER_CHOICE = [
        ['M','남성'],# <option value='M'>남성</option>
        ['F','여성'] # index 0: 전송될 값, index 1: 입력양식에 보여질 값.
    ]
    name = models.CharField(verbose_name='이름', max_length=100)
    email = models.EmailField(verbose_name='이메일', max_length=100)
    gender =models.CharField(verbose_name='성별', max_length=1, choices=GENDER_CHOICE)

    def __str__(self):
        return f"{self.pk}, {self.name}"
