from django.shortcuts import render
from .models import Choice, SubChoice, Question
from django.http import HttpResponse
# 질문 목록을 보여주는 View
# View 로직 순서.
# 1. 사용자가 보내준 값(있다면)에 대한 검증/타입 변경
# 2. Business Logic 처리.
# 3. 결과 응답

# http://127.0.0.1:8000/polls/list
def list(request):
    # business logic -> 질문 DB조회
    question_list = Question.objects.all().order_by('id')
    # print(question_list)
    
    # templates을 호출 - render(request, "template의 경로", [,{template에 전달할 값-dictionary}]) :템플릿을 호출
    

    return render(request, 
                 'polls/list.html',
                 {"question_list":question_list})
    # return HttpResponse(str(question_list))

# vote_form View(한개 질문에 대한 정보를 조회해서 응답.)
# def vote_form(request, question_id):
#     vote_info = Choice.objects.filter(question_id=question_id)
#     dic={}
#     for idx, q in enumerate(vote_info):
#         dic["{}".format(idx)] = q.choice_text
#     return HttpResponse(dic.items())

# vote_form View(한개 질문에 대한 정보를 조회해서 응답.)
def vote_form(request, question_id):
    print("vote_form", question_id)
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/vote_form.html',{"question": question})
    except:
        return render(request, 'polls/error.html', {"error_message":f"{question_id} is not existing question."})