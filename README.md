# blog_project
## 목차

1. 요구사항
2. 프로젝트 구조
3. 데이터베이스 구조
4. 기능명세서
5. 화면설계
6. 회고
---
### 요구사항명세
- 프로젝트 일정: 10월 26일(목) ~ 11월 7일(화)
- 11월 8일 개별 발표(개인당 5분)
- 기술 blog 만들기
- 모놀리식 (DRF는 이 프로젝트에서 사용하지 않습니다.)
- 데이터베이스 구조를 설계
<details>
<summary>1. 메인페이지 구현</summary>
- 페이지 제목과 블로그 입장하기 버튼이 있습니다.<br>
- 회원가입/로그인 버튼이 있습니다.<br>
- 회원가입 버튼을 클릭하면 회원가입 페이지로 이동합니다.<br>
- 로그인 버튼을 클릭하면 로그인 페이지로 이동합니다.<br>
</details>
<details>
<summary>2. 회원가입 기능 구현</summary>
- 회원가입을 할 수 있는 페이지가 있어야합니다.<br>
- 입력받는 값은 id, password입니다.<br>
</details>
<details>
<summary>3. 로그인 기능 구현</summary>
- 로그인을 할 수 있는 페이지가 있어야합니다.<br>
- 입력받는 값은 id, password입니다.<br>
</details>
<details>
<summary>4. 게시글 작성 기능 구현</summary>
- 로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.<br>
- 게시글 제목과 내용을 작성 할 수 있는 페이지가 있어야합니다.<br>
- 작성한 게시글이 저장되어 게시글 목록에 보여야 합니다.<br>
- 사진 업로드가 가능하도록 합니다.<br>
- 게시글 조회수가 올라갈 수 있도록 합니다.<br>
</details>
<details>
<summary>5. 게시글 목록 기능 구현</summary>
- 모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 할 수 있습니다.
</details>
<details>
<summary>6. 게시글 상세보기 기능 구현</summary>
- 게시글의 제목/내용을 보는 기능입니다.
</details>
<details>
<summary>7. 게시글 검색 기능 구현</summary>
- 주제와 태그에 따라 검색이 가능하게 합니다.<br>
- 검색한 게시물은 시간순에 따라 정렬이 가능해야 합니다.<br>
</details>
<details>
<summary>8. 게시글 수정 기능 구현</summary>
- 로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.<br>
- 본인의 게시글이 아니라면 수정이 불가능합니다.<br>
- 게시글의 제목 또는 내용을 수정 하는 기능입니다.<br>
- 게시글 제목과 내용을 수정 할 수 있는 페이지가 있어야합니다.<br>
- 수정된 내용은 게시글 목록보기/상세보기에 반영되어야합니다.<br>
</details>

<details>
<summary>9. 게시글 삭제 기능 구현</summary>
- 로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.<br>
- 본인의 게시글이 아니라면 수정이 불가능합니다.<br>
- 게시글을 삭제하는 기능입니다.<br>
- 삭제를 완료한 이후에 게시글 목록 화면으로 돌아갑니다.<br>
- 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하며,<br>
접근 시도 시 '존재하지 않는 게시글입니다' 라는 페이지를 보여줍니다.<br>
</details>

<details>
<summary>10. 회원 관련 추가 기능(UI 직접 구현 필요)</summary>
    - 비밀번호 변경기능<br>
    - 프로필 수정<br>
    - 닉네임 추가<br>
</details>

<details>
<summary>11. 댓글 기능(UI 직접 구현 필요)</summary>
- 댓글 추가<br>
- 댓글 삭제<br>
- 대댓글<br>
</details>

<details>
<summary>12. 부가 기능</summary>
- 번역 기능 (en, kr)
</details>
    
### WBS
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Django 기술블로그 
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section 전체
    요구사항 분석            :done,    des1, 2023-10-26, 0d
    데이터베이스 설계         :done,  des2, 2023-10-26, 0d
    개발                   :done, des3, after des2, 7d
    프레젠테이션             :active, des4, after des3, 2d

    section 개발
    회원가입 기능 구현        :done,    dev1, after des2, 0d
    로그인 기능 구현           :done, 1d
    게시글 CRUD 구현        :done,crit, 2d
    게시글 검색 기능            :done,0d
    회원 관련 추가 기능        :done,1d
    댓글 기능                :done,1d
    대댓글                   :done,12h
    마크다운 기능            :done,12h
    부가 기능                :done, 3h
    메인페이지 및 테마 구현     :done,1d
```
---
### 프로젝트 구조
- 4가지의 커스텀 앱과 2개의 외부 라이브러리를 사용합니다.
```python
INSTALLED_APPS = [
    ...
    # 커스텀 앱
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'main.apps.MainConfig',
    'django_tuieditor.apps.DjangoTUIEditorConfig',
    # 외부 라이브러리
    'bootstrap5',
    'django_bootstrap_icons',
]

```
- urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
```

---
### 데이터베이스 구조
```mermaid
erDiagram
    user ||--o{ post : write
    user {
      integer id PK
      varchar username
      varchar password
      image profile_image
      datetime created_at
      varchar ip_address
      datetime last_login
    }
    post }|--|{ tag : contains
    post ||--o| category : has
    post {
      integer id PK
      varchar title
      text content
      file file_upload
      image image_upload
      datetime created_at
      datetime updated_at
      varchar writer
      integer user_id FK
      integer hits
      integer tags FK
      varchar category FK
    }
    post ||--o{ comment : contains
    comment ||--o{ comment : contains
    comment {
      integer id PK
      integer parent FK
      text comment
      comment comment_reply FK
      datetime created_at
      datetime updated_at
    }
    
    tag {
      integer id PK
      varchar name
    }
    
    
    category {
      integer id PK
      varchar name
    }
```
- python modeling
```python
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
    
class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True)
    
class Post(BaseModel):
  title = models.CharField(max_length=100)
  content = MarkdownField()
  image_upload = models.ImageField(verbose_name='이미지',upload_to='blog/%Y/%m/%d/', blank=True, null=True)
  file_upload = models.FileField(verbose_name='파일',upload_to='file/%Y/%m/%d/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
  hits = models.IntegerField(default=0)
  category = models.ForeignKey(Category, blank=True, null=True ,on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, blank=True)

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment_reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
  comment_order = models.IntegerField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)


```

---
### 기능명세서
- CBV(Class Based View)로 작성되었습니다.
# 공통 상속 클래스
- 페이지의 제목을 나타내는 클래스를 만들고 모든 View가 상속하도록 했습니다.
```python
class PageTitleViewMixin:
  title = ""

  def get_title(self):
    return self.title
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.get_title()
    return context
```

# BoardList(PageTitleViewMixin, ListView)
- 작성된 글의 리스트화면 입니다.
- 페이지네이션, 검색, 삭제(관리자) 기능이 있습니다.
```python
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    count = len(self.object_list)
    category = Category.objects.all()
    
    context['count'] = count
    context['category'] = category
    
    return context
```
```python
def get_context_data(self, **kwargs):
    ...
    context = super().get_context_data(**kwargs)
    search = self.request.GET.get('search', '')
    sel_category = self.request.GET.get('category', '')
    sort = self.request.GET.get('sort', '')
        
    if search:
      context['search'] = search
    if sel_category:
      category = category.extra(select={'is_sel_category':'id = '+sel_category})
    
    context['category'] = category
    context['sort'] = sort

    return context
```
```python
  def get_queryset(self):
    queryset = super().get_queryset().annotate(number_of_comments=Count('comment'))
    
    search = self.request.GET.get('search', '')
    cate = self.request.GET.get('category', '')
    
    q = Q()
    if search:
      q &= (Q(title__icontains=search) | Q(content__icontains=search))
    if cate:
      q &= Q(category=cate)

    return queryset.filter(q)
```
```python
  def get_ordering(self):
    sort = self.request.GET.get('sort', 'created_at')
    ordering = ['-'+sort]    # sort = 'hits' or 'created_at'
    return ordering
```

# BoardWrite(PageTitleViewMixin, CreateView)

---
### 화면 설계
<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
                
![main](https://github.com/jmp7911/blog_project/assets/37658328/60d88cc3-0bff-404f-b828-6bfaae765d4d)
            </td>
            <td>
                ![로그인](https://github.com/jmp7911/blog_project/assets/37658328/65b7529d-aba2-4520-84bd-76ff241625ac)
            </td>
        </tr>
        <tr>
            <td>회원가입</td>
            <td>정보수정</td>
        </tr>
        <tr>
            <td>
                ![join](https://github.com/jmp7911/blog_project/assets/37658328/10542550-27b1-422c-b73d-55b4775e2def)
            </td>
            <td>
                ![profile](https://github.com/jmp7911/blog_project/assets/37658328/74b40359-df3b-42f6-9ce2-1a8b8d051b8c)
            </td>
        </tr>
        <tr>
            <td>검색</td>
            <td>번역</td>
        </tr>
        <tr>
            <td>
                ![search](https://github.com/jmp7911/blog_project/assets/37658328/9b4a2d2e-f52e-4156-8adb-94bcd52d8d7c)
            </td>
            <td>
                ![translate](https://github.com/jmp7911/blog_project/assets/37658328/24b1a364-9d1d-4bae-927c-c3dd06fbc4d6)
            </td>
        </tr>
        <tr>
            <td>선택삭제</td>
            <td>글쓰기</td>
        </tr>
        <tr>
            <td>![delete-muti](https://github.com/jmp7911/blog_project/assets/37658328/a5b97ba0-6fd1-4a32-8b7c-65ed3f34fa2f)
            </td>
            <td>
                ![write](https://github.com/jmp7911/blog_project/assets/37658328/062baf3d-0c03-4e46-a6a4-d19391231508)
            </td>
        </tr>
        <tr>
            <td>글 상세보기</td>
            <td>댓글</td>
        </tr>
        <tr>
            <td>
                ![detail](https://github.com/jmp7911/blog_project/assets/37658328/938215d9-86a2-4678-ae26-3fbedf771744)
            </td>
            <td>
                ![reply](https://github.com/jmp7911/blog_project/assets/37658328/a12781ff-2763-40da-a2ea-341eae9f56e7)
            </td>
        </tr>
    </tbody>
</table>


---
