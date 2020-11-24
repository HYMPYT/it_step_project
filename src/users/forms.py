from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number')


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def save(self, commit=True, user=None):
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.save()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name[0].isupper():
            raise forms.ValidationError('First name must contain the first capital letter')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name[0].isupper():
            raise forms.ValidationError('Last name must contain the first capital letter')
        return last_name

