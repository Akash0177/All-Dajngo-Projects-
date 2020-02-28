from django.shortcuts import render
from . import forms
# Create your views here.
def thankyouview(request):
    return render(request,'testapp/thankyou.html')

def feedbackview(request):
    form=forms.FeedBackForm()
    if request.method=='GET':
        form=forms.FeedBackForm()
        

    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and priting feedback info')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Rollno:',form.cleaned_data['rollno'])
            print('Student Emailid:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
    return render(request,'testapp/feedback.html',{'form':form})
