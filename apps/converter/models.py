from django.db import models
from django import forms
from validator import ExtFileField


class FileForm(forms.Form):
    class Meta():
        db_table = "form"
    CHOICES = (
        ('csv', 'csv'),
        ('json', 'json'),
        ('xml', 'xml')
        )
    # title = forms.CharField(max_length=50)
    select = forms.ChoiceField(choices=CHOICES, required=True, label='Convert to')
    # file = forms.FileField()
    file = ExtFileField(ext_whitelist=['csv', 'json', 'xml'])
# Create your models here.
