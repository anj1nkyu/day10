from django.shortcuts import render
from article.models import Article
from django.core.paginator import Paginator

def index(request):
  articles = Article.objects.all()
  paginator = Paginator(articles, 5)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'index.html', {'page_obj': page_obj})