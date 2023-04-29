from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "username...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "username...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "email...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "repeat password...",
                "class": "w-full py-4 px-4 rounded-xl"
            }
        )
    )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'profile_image',)

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "w-full py-2 px-4 rounded-xl border mb-2"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "w-full py-2 px-4 rounded-xl border mb-2"
            }),
            "bio": forms.Textarea(attrs={
                "class": "w-full py-2 px-4 rounded-xl mb-2 border"
            }),
            "profile_image": forms.FileInput(attrs={
                "class": '''block w-full border border-gray-200 shadow-sm rounded-md text-sm focus:z-10 focus:border-blue-100 focus:ring-blue-200 dark:bg-slate-200 dark:border-gray-500 dark:text-gray-400
                file:bg-transparent file:border-0
                file:bg-gray-100 file:mr-4
                file:py-3 file:px-4
                dark:file:bg-gray-500 dark:file:text-gray-100'''
            }),
        }
