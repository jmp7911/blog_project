from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .forms import UserJoinForm

class PageTitleViewMixin:
  title = ""

  def get_title(self):
    return self.title
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.get_title()
    return context
  
class JoinUser(PageTitleViewMixin, CreateView):
  title = '회원가입'
  template_name = 'accounts/join.html'
  success_url = settings.LOGIN_URL
  form_class = UserJoinForm
  
class loginUser(PageTitleViewMixin, LoginView):
  title = '로그인'
  template_name = 'accounts/login.html'
  


logout = LogoutView.as_view(
    next_page = settings.LOGIN_URL,
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
  
signup = JoinUser.as_view()
login = loginUser.as_view()