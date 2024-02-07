from django.contrib.auth.forms import UserCreationForm
from .views import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('custom_field1', 'custom_field2',)
