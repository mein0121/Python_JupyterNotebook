from django.shortcuts import render, redirect
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
def vote_form(request, question_id):
    print("vote_form", question_id)

    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/vote_form.html',
        {"question": question})
    except:
        return render(request, 'polls/error.html', 
        {"error_message":f"{question_id} is not existing question."})

# 투표처리 - 선택된 Choice의 vote값을 1증가
# /polls/vote
def vote(request):
    # 요청 파라미터 조회 + 검증
    # POST요청: request.POST.get('요청파라미터이름') or request.POST['이름']
    # GET요청 : request.GET.get('요청파라미터이름')  or request.GET['이름']
    choice_id = request.POST.get('choice')
    # 요청 파라미터 검증: choice로 넘어온 값이 없다면(None) 다시 vote_form으로 이동.
    question_search = request.POST.get('question_id')
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
    
    return redirect("/polls/vote_result/{}".format(choice.question_id))
    # return redirect(f"/polls/vote_result/{question_search}")

# 문제의 투표결과를 보여주는 view. /polls/vote_result/번호
def vote_result(request, question_id):
    #조회
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/vote_result.html", {"question": question})
# 문제의 투표결과를 보여주는 view. /polls/vote_result/번호
# def vote_result(request, question_id):
#     #조회
#     # question = Question.objects.get(pk=question_id)
#     choice =Choice.objects.get(pk=question_id)
#     return render(request, "polls/vote_result.html", {"choice": choice})
