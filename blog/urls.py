
from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^$' , views.index , name = 'index'),
#url(r'^search$' , views.search , name = 'search'),
url(r'^Create$' , views.Create , name = 'Create'),
url(r'^details$' , views.details , name = 'details'),
url(r'^body$' , views.body , name = 'body'),
]