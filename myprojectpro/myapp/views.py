from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.
def listview(request):
	all_articles = Article.objects.all()
	context = {
		'list':all_articles,
	}
	return render(request, 'myapp/list.html', context)

def detailview(request, id=None):
	article = get_object_or_404(Article, id=id)
	context = {
		'article':article,
	}
	return render(request, 'myapp/detail.html', context)