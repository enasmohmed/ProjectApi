from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationFormو NewUserForm
from django.contrib.auth.models import User





class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
        
            return user

