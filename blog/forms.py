from django import forms
from django.forms import ModelForm
from . import models
from .models import Post

class PostForm(forms.ModelForm):
	class Meta():
		model = models.Post
		fields = ('title' , 'author','body' )
