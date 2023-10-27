from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name
  
class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image_upload = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True)
  file_upload = models.FileField(upload_to='file/%Y/%m/%d/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  writer = models.CharField(max_length=100)
  hits = models.IntegerField(default=0)
  category = models.ForeignKey(Category, blank=True, null=True ,on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, blank=True)
  
  def __str__(self):
    return self.title
    
  def increase_views(self):
    self.hits += 1
    self.save(update_fields=['hits'])
    
    
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment_order = models.IntegerField(null=True, blank=True)
  comment_reply = models.IntegerField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  
  def __str__(self):
    return self.content
  
      
