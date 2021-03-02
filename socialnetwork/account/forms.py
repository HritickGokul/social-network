from django import forms
from django.contrib.auth import get_user_model
from account.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username' , 'email' , 'password1' , 'password2')
        model = get_user_model()

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

class UserForm(forms.ModelForm):
    class Meta:
        fields = ('username' , 'email')
        model = User

class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('image', 'bio')
        model = Profile
