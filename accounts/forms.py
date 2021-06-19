from django import forms
from .models import AppUsers
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class MyRegistrationForm(UserCreationForm):

	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	email = forms.EmailField(label='Enter email')
	password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	class Meta:
		model = AppUsers
		fields = ('username', 'email', 'password1', 'password2')

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise ValidationError("Username already exists")
		return username

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError("Password don't match")
		return password2

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise  ValidationError("Email already exists")
		return email

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()

		return user