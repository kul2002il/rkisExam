from django import forms

from .models import *


class LoginForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = UserProfile
		fields = 'username', 'password'


class UserProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	image = forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		fields = 'username', 'password', 'first_name', 'last_name', 'image', 'email'
