from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import customUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = customUser
        fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = customUser
        fields = UserChangeForm.Meta.fields