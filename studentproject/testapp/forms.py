from django import forms
from testapp.models import Student
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'
