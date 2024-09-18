from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length = 100)
	text = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		return self.text