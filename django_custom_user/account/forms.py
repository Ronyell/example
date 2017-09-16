from django import forms
from .import constants
from .models import Company
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    # Form Fields.
    username = forms.CharField(label=constants.USERNAME,
                               max_length=constants.USERNAME_MAX_LENGHT)

    email = forms.EmailField(label=constants.EMAIL)

    password = forms.CharField(widget=forms.PasswordInput,
                               label=_(constants.PASSWORD))

    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            label=_(constants.PASSWORD_CONFIRMATION))

    class Meta:
        model = Company
        fields = [
            'username',
            'first_name',
            'email',
            'location',
        ]
