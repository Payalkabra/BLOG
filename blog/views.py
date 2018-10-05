from django.shortcuts import render, redirect ,render_to_response
#from django.http import HttpResponse
from blog.models import Author , Post
from . import forms
from .forms import PostForm
from django.db.models import Q

# Create your views here.
#def index(request):
#	return HttpResponse("<h1></h1>")
def index(request):
	all_posts = Post.objects.all().order_by('-date')
	template_data = {'posts' : all_posts}

	return render_to_response('blog/index.html' , template_data)

#def search(request):
#	if request.method == "POST":
#		new_title = request.POST.get('title')
#		print(new_title)

#	return render_to_response('blog/search.html' , new_title)

def Create(request):
	if request.method == "POST":
		form = forms.PostForm(request.POST)
#		if form.is_valid():
#			f.save()
	else:
		form = forms.PostForm()
	return render(request , 'blog/Create.html' ,{'form':form})	

#def search(request):
#	query = request.GET.get('q')
#	results = Post.objects.filter(Q(title = query))

#	return render_to_response('blog/search.html' , results)
#	pass


def details(request):
	all_posts = Post.objects.all().order_by('-date')
	template_data = {'posts' : all_posts}

	return render_to_response('blog/details.html' , template_data)

def body(request):
	all_posts = Post.objects.all().order_by('-date')
	template_data = {'posts' : all_posts}

	return render_to_response('blog/details/body.html'  , template_data)

 