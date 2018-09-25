from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)

	def __str__(self):
		return "%s (%s)" % (self.name ,self.email)


class Post(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	author = models.ForeignKey('Author' , on_delete = models.CASCADE,)
	date = models.DateTimeField()

	def __str__(self):
		return "%s (%s)" % (self.title ,self.author.name)