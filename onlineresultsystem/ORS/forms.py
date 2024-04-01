from django import forms
from .models import User,developer

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class developer(forms.ModelForm):
    class Meta:
        model = developer
        fields = "__all__"