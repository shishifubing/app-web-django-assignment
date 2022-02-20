from django.urls import path
from .views import ArticleList, ArticleDetail


urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас
    # останется пустым, позже станет ясно почему
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде
    # view. Для этого вызываем метод as_view
    path('', ArticleList.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('<int:pk>', ArticleDetail.as_view()),

]
