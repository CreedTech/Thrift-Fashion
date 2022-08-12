from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User


class ProfileForm(UserCreationForm):
    # profile_image = forms.FileField(label='', widget=forms.FileInput(attrs={
    #     "class":"form-control rounded-0",
    #     "accept":"image/png, image/jpg, image/jpeg",
    #     "required":False
    # }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'phone_number', 'profile_image',)

    def _init_(self, *args: Any, **kwargs: Any) -> None:
        super(ProfileForm, self)._init_(*args, **kwargs)

        for fieldname in ('username', 'email', 'password1', 'password2', 'phone_number', 'profile_image', ):
            self.fields[fieldname].help_text = None
