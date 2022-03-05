from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleListSearch, ArticleCreateView, ArticleDeleteView, ArticleUpdateView


urlpatterns = [
    path(
        '',
        ArticleList.as_view(),
        name='article_root'),
    path(
        '<int:pk>',
        ArticleDetail.as_view(),
        name='article_detail'),
    path(
        'search',
        ArticleListSearch.as_view(),
        name='article_search'),
    path(
        'add/',
        ArticleCreateView.as_view(),
        name='article_create'),
    path(
        '<int:pk>/delete',
        ArticleDeleteView.as_view(),
        name='article_delete'),
    path(
        '<int:pk>/edit',
        ArticleUpdateView.as_view(),
        name='article_update')]
