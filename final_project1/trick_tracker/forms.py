from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields  # Adjust the fields as needed

class CustomUserUpdateForm(UserChangeForm):
    password = None  # Exclude the password field from the form

    class Meta:
        model = User
        fields = ['username', 'email']  # Specify the fields you want to include in the form
