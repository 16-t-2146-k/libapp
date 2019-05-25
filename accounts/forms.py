from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User_info


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User_info
        fields = ('username','last_name','first_name', 'is_staff',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User_info
        fields = ('username', 'is_staff')