from typing import Any
from .models import Post, Author
from django.forms import ModelForm, Form, DateField
from .widgets import XDSoftDatePickerInput


class FormMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        add extra attributes to all widgets
        """
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            _class = field.widget.attrs.get('class', '')
            extra = ' form-control'
            if hasattr(field.widget,
                       'input_type') and field.widget.input_type == 'checkbox':
                extra = ''
            field.widget.attrs.update({'class': _class + extra,
                                       'placeholder': f'...'})


class ViewMixin:
    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to access the current user
        """

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ArticleForm(FormMixin, ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'description', 'type', 'category')

    def save(self, commit=True):
        author = Author.objects.get_or_create(user=self.request.user)[0]
        self.instance.author = author
        return super().save(commit)


class DateFormXDSoft(Form):
    date = DateField(input_formats=['%d/%m/%Y'],
                     widget=XDSoftDatePickerInput())
