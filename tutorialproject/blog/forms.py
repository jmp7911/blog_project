from django import forms
from django.conf import settings
from .models import Post
from django.db import models
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ['title', 'content', 'file_upload', 'image_upload', 'tags', 'category']
    widgets = {
      'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
    }
