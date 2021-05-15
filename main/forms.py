from django import forms

from .models import *


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	image = forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		fields = 'username', 'password', 'first_name', 'last_name', 'image', 'email'
