from django import forms
from .models import IssueBook,BookStore,admin_login

class FormName(forms.Form):
    book_name = forms.CharField(required=False)
    book_author = forms.CharField(required=False)
    book_publisher= forms.CharField(required=False)

class IssueForm(forms.ModelForm):
    class Meta():
        model = IssueBook
        fields='__all__'

class IssueDetail(forms.ModelForm):
    class Meta():
        model = IssueBook
        fields= ['issueRollno']

class StudentLogin(forms.Form):
    rollno=forms.CharField(max_length=200)
    Password=forms.CharField(max_length=32, widget=forms.PasswordInput)
