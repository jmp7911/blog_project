from django import template
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
# from .forms import PostForm
from django.urls import reverse_lazy

from .models import Post, Category, Tag
from django.conf import settings
import markdown
from django.utils.safestring import mark_safe
from markdown.extensions.toc import TocExtension
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# content_type = ContentType.objects.get_for_model(Post)
# post_permission = Permission.objects.filter(content_type=content_type)
# print([perm.codename for perm in post_permission])
# ['add_post', 'change_post', 'delete_post', 'view_post']
class PageTitleViewMixin:
  title = ""

  def get_title(self):
    return self.title
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.get_title()
    return context
 
class BoardList(PageTitleViewMixin, ListView):
  title = '게시글 목록'
  model = Post
  paginate_by = 5
  context_object_name = 'post_list'
  
  def get_context_data(self, **kwargs):
    # request의 GET 파라미터에서 'q'를 가져옵니다.
    search = self.request.GET.get('search', '')
    sel_category = self.request.GET.get('category', '')
        
    context = super().get_context_data(**kwargs)
    count = len(self.object_list)
    category = Category.objects.all()
    
    
    if search:
      context['search'] = search
    if sel_category:
      category = category.extra(select={'is_sel_category':'id = '+sel_category})
    
    context['count'] = count
    context['category'] = category
    
    return context
  
  def get_queryset(self):
    queryset = super().get_queryset()

    # request의 GET 파라미터에서 'q'를 가져옵니다.
    search = self.request.GET.get('search', '')
    cate = self.request.GET.get('category', '')
    
    q = Q()
    # 'q' 파라미터가 제공되었을 경우, 쿼리셋을 필터링합니다.
    if search:
      q &= (Q(title__icontains=q) | Q(content__icontains=q))
    if cate:
      q &= Q(category=cate)
      
    return queryset.filter(q)
  
  def get_ordering(self):
    sort = self.request.GET.get('sort', 'created_at')
    ordering = ['-'+sort]
    return ordering
    
class BoardWrite(PageTitleViewMixin, CreateView):
  # form_class = PostForm
  permission_required = 'blog.add_post'
  title = '게시글 작성'
  model = Post
  fields = ['title', 'content', 'file_upload', 'image_upload', 'tags', 'category']
  context_object_name = 'post'
  
class BoardUpdate(PageTitleViewMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'blog.change_post'
  title = '게시글 수정'
  model = Post
  fields = ['title', 'content', 'file_upload', 'image_upload', 'tags', 'category']
  context_object_name = 'post'
class BoardView(PageTitleViewMixin, DetailView):
  title = '게시글 보기'
  model = Post
  context_object_name = 'post'
  
  def get(self, request, *args, **kwargs):
    response = super(BoardView, self).get(request, *args, **kwargs)

    self.object.increase_views()

    return response
  def get_object(self, queryset=None):
    post = super(BoardView, self).get_object(queryset=None)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.content = md.convert(post.content)
    post.toc = md.toc
    return post
  
class BoardDelete(PageTitleViewMixin, PermissionRequiredMixin, DeleteView):
  permission_required = "blog.delete_post"
  title = '게시글 삭제'
  model = Post
  context_object_name = 'post'
  success_url = reverse_lazy('blog')
  
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)
    
def chat(request):
  return render(request, 'blog/chat.html')

class BoardDeleteMultiple(View):
  title = '게시글 선택 삭제'
  
  def post(self, *args, **kwargs):
    print(f'request: {self.request.POST}')
    
    if self.request.user.is_staff:
      data = self.request.POST.get('data[]')
      
      Post.objects.filter(id__in=data).delete()
    return redirect('blog')
  
index = BoardList.as_view()
write = login_required(BoardWrite.as_view())
update = BoardUpdate.as_view()
view = BoardView.as_view()
delete = BoardDelete.as_view()