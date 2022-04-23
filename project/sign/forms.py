from django.contrib.auth.forms import UsernameField
from django.forms import CharField, PasswordInput, TextInput, BooleanField
from typing import Any
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    first_name = CharField(label='First name')
    last_name = CharField(label='Last name')

    error_css_class = 'alert alert-danger'
    required_css_class = 'alert alert-danger'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        _class = {'class': 'form-control form-control-user'}
        self.fields['username'].widget.attrs.update({
            **_class, 'placeholder': 'Enter username'})
        self.fields['email'].widget.attrs.update({
            **_class, 'placeholder': 'Enter email'})
        self.fields['first_name'].widget.attrs.update({
            **_class,
            'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({
            **_class,
            'placeholder': 'Enter your last name'})
        self.fields['password1'].widget.attrs.update({
            **_class,
            'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({
            **_class,
            'placeholder': 'Repeat your password'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class CustomLoginForm(LoginForm):

    login = UsernameField(
        label='',
        widget=TextInput(attrs={"autofocus": True}))
    password = CharField(
        label='',
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "current-password"}))
    remember = BooleanField(label='Remember Me',
                            required=False)

    error_css_class = 'alert alert-danger'
    required_css_class = 'alert alert-danger'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _class = {'class': 'form-control form-control-user'}
        self.fields['login'].widget.attrs.update({
            **_class, 'placeholder': 'Enter username'})
        self.fields['password'].widget.attrs.update({
            **_class, 'placeholder': 'Enter password'})
        self.fields['remember'].widget.attrs.update({
            **{'class': 'custom-control-input'}})
