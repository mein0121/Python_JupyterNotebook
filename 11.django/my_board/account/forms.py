from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.db.models import fields # settings.py에 등록된 AUTH_USER_MODEL 클래스를 반환.
from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput
# CustomUser와 연동된 ModelForm
class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    # password1 = forms.PasswordInput()
    password2 = forms.CharField(label='Password 확인',widget=PasswordInput())
    # password2 = forms.PasswordInput() # 위 설정없이 field에 변수명입력하면 기본으로 입력

    class Meta:
        # model = CustomUser # model에정의한 CustomUser import후 사용가능.
        model = get_user_model()
        fields = ['username', 'password1', 'password2','name','email','gender']
        # fields = '__all__'
        # model의 Field들의 widget(입력양식)을 변경하고자 할때 widgets 속성을 딕셔너리에 등록한다.(field명:widget객체)
        widgets = {
            "name":forms.Textarea,
        }