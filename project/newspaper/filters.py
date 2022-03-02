from django_filters import FilterSet, DateTimeFilter, CharFilter
from .models import Article
from .widgets import BootstrapDatePickerInput, BootstrapTextInput


class ArticleFilter(FilterSet):

    publication_date = DateTimeFilter(
        lookup_expr='gte', label='',
        # DATETIME_INPUT_FORMATS, settings.py
        widget=BootstrapDatePickerInput(format='%Y-%m-%D'))
    name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=BootstrapTextInput(_placeholder='article name'))
    author_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=BootstrapTextInput(_placeholder='author name'))

    class Meta:
        model = Article
        fields = ['publication_date', 'name']
