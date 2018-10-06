from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=40)
	content = models.TextField()
	author = models.CharField(max_length=40)
	created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']