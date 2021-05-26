from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField

# Question (질문)
#   - question_text(질문내용)
#   - pub_date(질문 등록 일시)
#   - id(PK - 자동생성): 1씩 증가하는 값을 가지도록 처리.
# Choice(질문에 대한 답변(보기))
#   - choice_text(보기내용)
#   - vote(몇번 선택되었는지)
#   - question(어떤 질문에 대한 보기인지 - Question의 FK)
#   - id(PK - 자동생성): 1씩 증가하는 값을 가지도록 처리.


# Model을 상속 
# 컬럼과 연결된 Field들을 class변수로 선언.
class Question(models.Model):
    # 변수명: 컬럼명, 값 : Field 객체타입 => 타입
    question_text = models.CharField(max_length=200) # CharField = NVACHAR
    pub_date = models.DateTimeField(auto_now_add=True) # auto_now_add: insert될때 일시를 자동등록
    
    def __str__(self):
        return self.question_text

    # class Meta:
    #     ordering = ['pub_date']
    
class Choice(models.Model):
    # no = models.IntegerField(primary_key=True)
    # choice_id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    vote = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE) # to : 참조 Model클래스 지정.
                                                                        # on_delete: 부모 테이블의 값이 delete될 경우 처리방식. CASCADE: 참조하는 자식데이터도 같이 삭제.

    def __str__(self):
        return self.choice_text

class SubChoice(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    sub_choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    
    
    def __str__(self):
        return self.description