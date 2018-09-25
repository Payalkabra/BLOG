from django.shortcuts import render_to_response
#from django.http import HttpResponse
from blog.models import Author , Post


# Create your views here.
#def index(request):
#	return HttpResponse("<h1></h1>")
def index(request):
	all_posts = Post.objects.all().order_by('-date')
	template_data = {'posts' : all_posts}

	return render_to_response('blog/index.html' , template_data)
