from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print('Total form Validation..')
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks Bot..!!!')

        inputname=cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name sholud compulsory contain minimum 10 characters')

        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno))!=3:
            raise forms.ValidationError('Rollno should contain exactly 3 digits')

        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('Passwords not matched')
