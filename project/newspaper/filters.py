from django_filters import FilterSet, DateTimeFilter, CharFilter
from .models import Post
from .widgets import BootstrapDatePickerInput, BootstrapTextInput


class ArticleFilter(FilterSet):

    # settings.py: DATETIME_INPUT_FORMATS
    publication_date = DateTimeFilter(
        lookup_expr='gte', label='',
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
        model = Post
        fields = ['publication_date', 'name', 'author_name']
