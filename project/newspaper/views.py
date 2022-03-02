from django.views.generic import ListView, DetailView
from .filters import ArticleFilter
from .models import Article
from django.core.paginator import Paginator

# Create your views here.


class ArticleList(ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-publication_date']
    paginate_by = 5


class ArticleListSearch(ArticleList):

    template_name = 'articles/articles_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(
            self.request.GET,
            queryset=self.get_queryset())
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
