from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import Post
# from django.core.paginator import Paginator

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

    # 페이징 처리
    # class변수: paginate_by = 한페이지의 데이터 개수
    # 요청시 url : url?page=번호 http://127.0.0.1:8000/board/list?page=2 page를 생략하면 1번페이지를 조회.
    # 페이지 번호를 template에서 출력하기 위한 값들을 만들어서 template에 전달. => get_context_data()를 오버라이딩
    paginate_by = 10
    
    # context data: view가 template에게 전달하는 값(dictionary). 
    # key_value쌍. key: context name, value: context value
    # get_context_data(): Generic View를 구현할때 template에게 추가적으로 전달해야하는 context data가 있을때 오버라이딩.
    
    # 페이징 관련 값들을 context data에 추가
    #   - 이전/다음 페이지 그룹 유무(그룹의 시작페이지의 이전/끝페이지의 다음)
    #   - 이전/다음 페이지 번호(그룹의 시작/끝페이지)
    #   - 현재 페이지 속한 페이지 그룹의 페이지 범위(시작 ~ 끝 페이지 번호)
    def get_context_data(self, **kwargs):
        # 부모객체의 get_context_data()를 호출해서 Generic View가 자동으로 생성한 Context data를 받아온다.
        context = super().get_context_data(**kwargs)
        # ListView에서 paginated_by속성을 설정하면 context data에 Paginator객체가 등록된다.
        paginator = context['paginator']
        page_group_count = 10 # 페이지 그룹에 속한 페이지 수.
        current_page = int(self.request.GET.get('page', 1))
        #CBV에서 HttpRequest는 self.request로 사용할 수 있다.

        # 페이지 그룹에 페이지 범위를 조회.
        #현재 페이지가 속한 그룹의 시작 페이지의 인덱스
        start_index = int((current_page-1)/page_group_count) * page_group_count
        #현재 페이지가 속한 그룹의 마지막 페이지의 인덱스
        end_index = start_index + page_group_count
        page_range = paginator.page_range[start_index:end_index]

        #그룹의 시작페이지가 이전페이지가 있는지 그룹의 마지막 페이지가 다음페이지가 있는지 여부 + 페이지 번호.
        start_page = paginator.page(page_range[0]) # 시작페이지의 page객체
        end_page = paginator.page(page_range[-1]) #  마지막페이지의 page객체
        has_previous = start_page.has_previous() # 시작의 이전페이지가 있는지 여부.
        has_next = end_page.has_next()

        context['page_range'] = page_range
        if has_previous:
            context['has_previous'] = has_previous
            context['previous_page_no'] = start_page.previous_page_number # 시작페이지 이전페이지 번호.
        if has_next:
            context['has_next'] = has_next
            context['next_page_no'] = end_page.next_page_number # 마지막 페이지의 다음페이지 번호
         
        return context
