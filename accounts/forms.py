from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser')
