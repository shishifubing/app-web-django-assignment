from django.views.generic import ListView, DetailView

from .models import Article

# Create your views here.


class ArticleList(ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('id')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
