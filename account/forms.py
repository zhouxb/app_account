from django import forms
from account.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'is_active', 'groups')
        widgets = {
            'username':forms.TextInput(attrs={'readonly':'readonly'}),
        }

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

