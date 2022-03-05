from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import ArticleForm
from .filters import ArticleFilter
from .models import Article

# Create your views here.


class ArticleList(ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-publication_date']
    paginate_by = 10

# https://cheat.readthedocs.io/en/latest/django/filter.html


class ArticleListSearch(ListView):

    model = Article
    template_name = 'articles/articles_search.html'
    context_object_name = 'articles'
    ordering = ['-publication_date']
    paginate_by = 5
    filterset_class = ArticleFilter
    form_class = ArticleForm

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filter'] = self.filterset
        context['form'] = self.form_class()
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_update.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()
    success_url = '/news/search'
