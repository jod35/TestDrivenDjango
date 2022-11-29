from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username','email','password1','password2']