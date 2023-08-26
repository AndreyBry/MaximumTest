from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.CharField(label='Почта')
    password1 = forms.CharField(label='Пароль', help_text='')
    password2 = forms.CharField(label='Подтверждение пароля')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control from-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control from-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control from-control-lg'
        self.fields['email'].widget.attrs['class'] = 'form-control from-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control from-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control from-control-lg'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
