from .models import Article
from django.forms import ModelForm, Form, DateField, DateTimeField, CharField
from .widgets import BootstrapDatePickerInput, BootstrapTextInput, XDSoftDatePickerInput


class ArticleForm(ModelForm):
    name = CharField(
        label='', widget=BootstrapTextInput(_placeholder='article name'))
    author_name = CharField(
        label='', widget=BootstrapTextInput(_placeholder='author name'))
    description = CharField(
        label='', widget=BootstrapTextInput(_placeholder='content'))

    class Meta:
        model = Article
        fields = ['name', 'author_name', 'description']


class DateFormXDSoft(Form):
    date = DateField(
        input_formats=['%d/%m/%Y'],
        widget=XDSoftDatePickerInput()
    )
