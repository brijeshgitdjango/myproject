from django.contrib import admin

# Register your models here.
from .models import Article

class AdminArticle(admin.ModelAdmin):
	list_display = ['title', 'author', 'created_on']
	list_editable = ['author']


admin.site.register(Article,AdminArticle)