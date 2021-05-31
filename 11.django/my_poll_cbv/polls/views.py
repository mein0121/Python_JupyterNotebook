from django.shortcuts import render, redirect
from .models import Choice, SubChoice, Question
from django.http import HttpResponse

from django.urls import reverse # reverse함수: path설정 이름으로 url문자열을 만들어주는 함수.
from django.views.generic import ListView, View, DetailView

# 질문 목록을 보여주는 View
# View 로직 순서.
# 1. 사용자가 보내준 값(있다면)에 대한 검증/타입 변경
# 2. Business Logic 처리.
# 3. 결과 응답

# # ListView - 모델의 전체 데이터를 조회해서 template에게 전달. (Paging기능 제공)
# class QuestionListView(ListView):
#     model = Question # 전체데이터를 조회할 모델클래스 지정.
#     template_name = "polls/list.html" # 응답할 template 경로
#     # 전체 조회결과를 template에 전달 - 이름: '모델클래스명(소문자)_list' or 'object_list' 
#     # 다른이름으로 template에 전달할 경우: context_object_name = '전송할이름'


# 투표작업을 처리
# GET요청 : 투표 양식(vote_form)
# POST요청 : 투표처리(vote)
class VoteView(View):
    # GET방식 요청 처리
    def get(self, request, *args, **kwargs):
        # kwargs: path parameter를 조회.
        question_id = kwargs['question_id']
        try:
            question = Question.objects.get(pk=question_id)
            return render(request, 'polls/vote_form.html',
            {"question": question})
        except:
            return render(request, 'polls/error.html', 
            {"error_message":f"{question_id} is not existing question."})
    # POST방식 요청 처리
    def post(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        choice_id = request.POST.get('choice')
    
    # 요청 파라미터 검증: choice로 넘어온 값이 없다면(None) 다시 vote_form으로 이동.
        # question_search = request.POST.get('question_id')
        question_search = kwargs['question_id'] # path parameter 조회
        if choice_id == None:
            question = Question.objects.get(pk=question_search)
            return render(request, "polls/vote_form.html",
                        {
                            "question":question,
                            "error_message":"보기를 선택하세요."
                        })

        # print(type(request.POST),choice_id, request.POST['choice'])
        # Business logic 처리 - 투표 처리.
        # update할 보기(Choice)를 조회
        choice = Choice.objects.get(pk=choice_id)
        # vote의 값을 1증가
        choice.vote += 1
        # update
        choice.save() # pk가 있으면 update, 없으면 insert.
        
        # 결과 응답       "url 설정 이름"       args=[path파라미터에 전달할 값,...,...,..]
        url_str = reverse("polls:vote_result", args=[choice.question_id])
        return redirect(url_str)


# DetatilView: 특정 모델의 Primary key를 받아서 조회한 결과를 template에 전달.
# # Primary key는 path parameter로 받아야 한다. urls.py에서 path parameter의 변수명은 <타입:pk>
# # question의 id(pk)를 받아서 질문하나를 조회한후에 template(vote_result.html)로 이동
# class QuestionDetailView(DetailView):
#     model = Question # 데이터를 조회할 Model 클래스 지정.
#     template_name = "polls/vote_result.html"