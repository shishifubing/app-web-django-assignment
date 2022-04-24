from typing import Any
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import ArticleForm, ViewMixin
from .filters import ArticleFilter
from .models import Post


class ArticleList(ListView):
    model = Post
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-publication_date']
    paginate_by = 10

# https://cheat.readthedocs.io/en/latest/django/filter.html


class ArticleListSearch(ListView):

    model = Post
    template_name = 'articles/search.html'
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
    model = Post
    template_name = 'articles/article.html'
    context_object_name = 'article'


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'articles/forms/update.html'
    model = Post
    form_class = ArticleForm
    permission_required = ('newspaper.change_article',)


class ArticleCreateView(PermissionRequiredMixin, ViewMixin, CreateView):
    template_name = 'articles/forms/create.html'
    form_class = ArticleForm
    permission_required = ('newspaper.add_article',)


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'articles/forms/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/search'

    permission_required = ('newspaper.delete_article',)
