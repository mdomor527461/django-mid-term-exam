from django import forms
from . import models
class CommentedForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']