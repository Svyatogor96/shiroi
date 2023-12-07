from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Описываем формы это нужно для более удобной работы с моделями

class LogInForm(AuthenticationForm):

    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя пользователя'}))

    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Пароль'}))


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя'}))
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя пользователя'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label='repassword', widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Повтор пароля'}))
    email = forms.CharField(label='email', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class CreatePatyForm(forms.ModelForm):

    def get_absolute_url(self):
        return f'party/index.html'

    class Meta:
        model = Party
        fields = ['title', 'description', 'dt',
                  'countPeople', 'adres', 'images']
        widgets = {
            'title': forms.TextInput(attrs={'class': '', }),

            'dt': forms.DateInput(attrs={'class': '', 'id': "airdatepicker"}),
        }
