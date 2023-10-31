from django import forms
from django.conf import settings
from .models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.contrib.auth import get_user_model

class UserJoinForm(UserCreationForm):
  
  class Meta:
    model = get_user_model()
    fields = ['email', 'nickname', 'profile_image' ]
    field_classes = {"email": UsernameField}
    
class UserProfileForm(UserChangeForm):
  
  class Meta:
    model = get_user_model()
    fields = ['email', 'nickname', 'profile_image']
    field_classes = {"email": UsernameField}