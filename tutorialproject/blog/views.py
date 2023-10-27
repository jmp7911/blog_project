from django.shortcuts import render

def index(request):
  return render(request, 'blog/index.html')
def chat(request):
  return render(request, 'blog/chat.html')
def view(request):
  return render(request, 'blog/view.html')
def write(request):
  return render(request, 'blog/write.html')