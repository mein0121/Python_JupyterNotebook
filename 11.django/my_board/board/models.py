from django.db import models

# Create your models here.

# 글의 카테고리
class Category(models.Model):
    # pk-자동증가 정수 컬럼
    category_code = models.BigAutoField(primary_key=True)
    # Charfiled() 문자열 필드 # verbose_name : 화면에 나올때 라벨명.
    category_name = models.CharField(max_length=200, verbose_name="글 카테고리")
    
    def __str__(self):
        return f"{self.category_name}"

# 게시물(글)
# title(제목), content(글내용), create_at(등록 일시), update_at(수정 일시), writer(글쓴사람-후에 추가)
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="글제목")# NOT NULL, 빈문자열을 허용 X
    content = models.TextField(verbose_name="글내용") # TextField: 대용량 text
    # null=False(default): not null 여부 - False: Not Null, True: null 허용 컬럼
    # blank=False(default): 빈 문자열 허용 여부. False: 허용안함, True: 허용
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, verbose_name="글 분류", null=True, blank=True)
    # 작성일시
    # auto_now_add=True(default:False) => insert 시점의 일시를 저장하고 그 이후에는 update하지 않는다.
    create_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    # 수정일시
    # auto_now=True(default:False) => insert/update할 때마다 그시점의 일시를 저장.
    update_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    def __str__(self):
        return f"{self.pk}, {self.title}"