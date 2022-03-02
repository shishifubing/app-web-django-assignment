from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleListSearch


urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
    path('search', ArticleListSearch.as_view())
]
