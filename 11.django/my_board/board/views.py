from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
# 글등록

# CreateView 등록(저장-insert 처리)
#   get방식 요청: 입력양식 화면으로 이동(render())
#   post방식요청: 입력(등록) 처리. \
#                처리성공: 성공페이지로 이동(redirect)
#                처리실패: 입력양식 화면으로 이동(render())
class PostCreateView(CreateView):
    template_name = 'board/post_create.html' # 입력양식 화면 template경로.
    form_class = PostForm # 요청 파라미터를 처리할 Form을 지정.
    # success_url = reverse_lazy('board:detail') # 등록 처리후 이동할 경로 -> redirect 방식 이동 => view의 url을 등록.
    # success_url 설정을 대신
    # success_url에서 insert한 Model객체를 접근하려면 이 메소드를 overriding 해야한다.
    # insert한 모델객체 조회: self.object
    def get_success_url(self):
        # 반환값: 등록 성공후 redirect방식으로 이동할 view의 url을 문자열로 반환.
        return reverse_lazy('board:detail', args=[self.object.pk]) # args: path parameter로 전달할 값들을 리스트에 순서대로 담는다.

# 하나의 글 정보 조회(pk)
# DetailView - pk로 조회한 결과를 template으로 보내주는 generic View
# url 패턴: pk를 path파라미터로 받는다. <type:pk> 변수명을 pk로 지정해야한다. 이 path파라미터 값을 이용해 select한다.
class PostDetailView(DetailView):
    template_name = "board/post_detail.html" # 응답할 template의 경로.
    model = Post # pk로 조회할 Model클래스. 조회결과를 "post"(모델클래스 명의 소문자),"object" 라는 이름으로 template에게 전달.

# path("detail/<int:pk>", DetailView.as_view(template_name='board/post_detail.html', model=Post), name='detail')

# 글 수정처리
# UpdateView
# - GET  요청처리: pk로 수정할 정보를 조회해서 template(수정 form)으로 전달(render())
# - POST 요청처리: Update 처리. redirect방식으로 view를 요청
# - tempate_name: 수정 form template파일의 경로
# - form_class: Form/ModelForm 클래스 등록
# - model: Model 클래스 등록 (수정 form template에 전달할 값을 조회하기 위해).
# - success_url: 수정 처리후 redirect방식으로 이동할 View의 url(path parameter로 update한 Model정보를 사용한 경우 get_success_url()를 오버라이딩.)
class PostUpdateView(UpdateView):
    template_name = "board/post_update.html"
    form_class = PostForm
    model = Post

    def get_success_url(self):
        return reverse_lazy('board:detail', args=[self.object.pk])


# 삭제처리
# generic view: DeleteView를 사용 => 삭제 확인 화면을 거쳐서 삭제 처리한다.
# 함수 기반으로 작성. path parameter로 삭제할 글의 id(pk)를 받아서 삭제 처리.
def post_delete(request, pk):
    # try
    post = Post.objects.get(pk=pk) # 삭제할 데이터를 조회.
    # except:
    # 에러페이지 이동
    post.delete() #post객체의 pk와 동일한 데이터를 삭제
    return redirect("/")

# 글 목록
# ListView 구현
# template_name: 결과를 보여줄 template의 경로
# model: 조회할 모델 클래스를 지정
# 조회결과를 template에 "object_list", "모델 이름 소문자_list(post_list)"라는 이름으로 전달.
# ListView는 paging기능 지원
class PostListView(ListView):
    template_name = "board/post_list.html"
    model = Post
