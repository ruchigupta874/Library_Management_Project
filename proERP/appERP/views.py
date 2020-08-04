# Create your views here.
from django.urls import reverse_lazy
from datetime import date
datetimeFormat = '%Y-%m-%d'
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import BookStore,Author,Publisher,Language,Genre,Student,Course,IssueBook,admin_login
from .forms import FormName,IssueForm,IssueDetail,StudentLogin
from django.db.models import Q # FOR COMPLEX SQL QUERY
from django.db.models import F # FOR DECREMENTING VALUE FROM MODELS
from django.shortcuts import get_object_or_404

## 127.0.0.0 PAGE ##
class indexView(View):
    def get(self,request):
        return render(request, 'index.html')
## STUDENT PORTAL  ##
## AFTER STUDENT LOGIN INDEX PAGE ##
class StudentHomeView(View):
    def get(self,request):
        return render(request,'login_home.html')

## BOOK SEARCH ##
def form_view(request):
    form=FormName()
    result = " "
    if request.method == 'POST':
        form=FormName(request.POST)
        if form.is_valid():
            author=form.cleaned_data['book_author']
            publisher=form.cleaned_data['book_publisher']
            bookName=form.cleaned_data['book_name']

        if publisher and author and bookName:
            result = BookStore.objects.filter(book_author__author_name=author, book_publisher__publisher_name=publisher,book_name__contains=bookName)
        elif not publisher and not author and not bookName:
            print("Expects atleast one field !")
        elif not author and not publisher:
            result = BookStore.objects.filter(book_name__contains=bookName)
        elif not author and not bookName:
            result = BookStore.objects.filter(book_publisher__publisher_name=publisher)
        elif not publisher and  not bookName:
            result = BookStore.objects.filter(book_author__author_name=author)
        elif not publisher:
            result = BookStore.objects.filter(book_author__author_name=author, book_name__contains=bookName)
        elif not bookName:
            result = BookStore.objects.filter(book_author__author_name=author, book_publisher__publisher_name=publisher)
        elif not author:
            result = BookStore.objects.filter(book_publisher__publisher_name=publisher,book_name__contains=bookName)
        else:
            print("Sorry we didn't understand your query!")
    args={'insert_me':form,'text':result}
    return render(request,'form_index.html', args)
## STUDENT LOGIN VALIDATION ##
def login_student(request):
    result = ''
    out = ''
    display =''
    template = 'student_login.html'
    form = StudentLogin()
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        if form.is_valid():
            rollno = form.cleaned_data['rollno']
            password = form.cleaned_data['Password']
            if admin_login.objects.filter(l_rollno=rollno, l_password=password):
                var = admin_login.objects.filter(l_rollno__student_rollno=rollno).values_list('l_rollno__student_name')
                display = f'Hello {var[0][0]}'
                result = 'Good Match'
                template = 'student_basic.html'
            else:
                result = 'Username or Password does not match ! Please Try again ..'
                template = 'student_login.html'
    args = {'insert_me': form, 'text': result, 'output': display}
    return render(request, template, args)



##### ADMIN PORTAL #####
## AFTER ADMIN LOGIN INDEX PAGE ##
class homeView(View):
    def get(self,request):
        return render(request,'Login_Home.html')

## Author , Publisher , Genre , Lanuguage , Book update,create,delete view ##
class AuthorListView(ListView):
    model = Author
    context_object_name = 'auth_list'
    template_name = 'author_list.html'
class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author_create.html'
class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'author_create.html' # TEMPLATE NAME IS SAME AS CREATE VIEW
class AuthorDeleteView(DeleteView):
    # by default context name=lower case model name
    model = Author
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:list')

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'pub_list'
    template_name = 'publisher_list.html'
class PublisherCreateView(CreateView):
    model = Publisher
    fields = ('publisher_name','publisher_description')
    template_name = 'publisher_create.html'
class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ('publisher_name','publisher_description')
    template_name = 'publisher_create.html'
class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:pub_list')

class LanguageListView(ListView):
    model = Language
    context_object_name = 'lan_list'
    template_name = 'language_list.html'
class LanguageCreateView(CreateView):
    model = Language
    fields = '__all__'
    template_name = 'language_create.html'
class LanguageUpdateView(UpdateView):
    model = Language
    fields = '__all__'
    template_name = 'language_create.html'
class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:lan_list')

class GenreListView(ListView):
    model = Genre
    context_object_name = 'gen_list'
    template_name = 'genre_list.html'
class GenreCreateView(CreateView):
    model = Genre
    fields = '__all__'
    template_name = 'genre_create.html'
class GenreUpdateView(UpdateView):
    model = Genre
    fields = '__all__'
    template_name = 'genre_create.html'
class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:gen_list')

class BookListView(ListView):
    model = BookStore
    context_object_name = 'book_list'
    template_name = 'book_list.html'
class BookCreateView(CreateView):
    model = BookStore
    fields = '__all__'
    template_name = 'book_create.html'
class BookUpdateView(UpdateView):
    model = BookStore
    fields = '__all__'
    template_name = 'book_create.html'
class BookDeleteView(DeleteView):
    model = BookStore
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:book_list')

class CourseListView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'course_list.html'
class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'course_create.html'
class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'course_create.html' # TEMPLATE NAME IS SAME AS CREATE VIEW
class CourseDeleteView(DeleteView):
    # by default context name=lower case model name
    model = Course
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:course_list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'student_list.html'
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_create.html'
class StudentUpdateView(UpdateView):
    model = Student
    fields = ('student_rollno','student_phone_number','student_address')
    template_name = 'student_create.html'
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete.html'
    success_url = reverse_lazy('appERP:stu_list')

## ISSUE REPORT ##
class IssueBookListView(ListView):
    model = IssueBook
    context_object_name = 'issue_list'
    template_name = 'issue_list.html'

## ISSUE BOOK ##
def issue_view(request):
    result='EMPTY'
    form=IssueForm()
    if request.method == 'POST':
        form=IssueForm(request.POST)
        if form.is_valid():
            roll_no =form.cleaned_data['issueRollno']
            book_name =form.cleaned_data['issueBookName']
            if IssueBook.objects.filter(Q(issueBookName__book_name=book_name) & Q(issueRollno=roll_no)):
                result = "Student can't issue same book more than one"
            elif IssueBook.objects.filter(~Q(issueBookName__book_name=book_name) & Q(issueRollno=roll_no)):
                var = BookStore.objects.get(book_name=book_name)
                var.book_copies = F('book_copies') -1
                var.save()
                form.save()  # SAVING DATA TO MODEL
                result="Book Issued Successfully "
            elif IssueBook.objects.filter(Q(issueBookName__book_name=book_name) & ~Q(issueRollno=roll_no)):
                var = BookStore.objects.get(book_name=book_name)
                var.book_copies = F('book_copies') -1
                var.save()
                form.save()
                result="Book Issued Successfully"
            elif IssueBook.objects.filter(~Q(issueBookName__book_name=book_name) & ~Q(issueRollno=roll_no)):
                var = BookStore.objects.get(book_name=book_name)
                var.book_copies = F('book_copies') -1
                var.save()
                form.save()
                result="Book Issued Successfully"
            else:
                result="Sorry didnt understand your query !"

    args = {'insert_me': form, 'text': result}
    return render(request, 'issue_form_index.html', args)

## ISSUE/RETURN/CALCULATE FINE DISPLAY
def StudentIssueDetail(request):
    issue_book_obj=''
    form_instance = IssueDetail()
    if request.method == 'POST':
        form_instance = IssueDetail(request.POST)
        if form_instance.is_valid():
            rollNo = form_instance.cleaned_data['issueRollno']
            issue_book_obj = IssueBook.objects.filter(issueRollno=rollNo)
            for i in range(len(issue_book_obj)):
                delta = date.today() - issue_book_obj[i].return_date
                if delta.days > 0:
                    issue_book_obj[i].fine = delta.days * 10
                else:
                    issue_book_obj[i].fine = 0


    args = {'insert_me': form_instance, 'text':issue_book_obj}
    return render(request, 'student_issue_detail.html', args)


def  student_issue(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        book = IssueBook.objects.filter(issueRollno = username)


        for i in range(len(book)):
            delta = date.today() - book[i].return_date
            if delta.days > 0:
                book[i].fine = delta.days * 10
            else:
                book[i].fine = 0
        context_dict = {'books': book}
        return render(request, 'student_fine.html', context_dict)



## RETURNING BOOK AND ADDING THAT BOOK TO DATABASE ##
def IssueDelete(request,pk):
    var1=IssueBook.objects.get(pk=pk)
    print(var1)

    if request.method=="POST":
        var1.delete()
        bookOBJ=BookStore.objects.get(book_name=var1)
        bookOBJ.book_copies = F('book_copies') + 1
        bookOBJ.save()
        return HttpResponseRedirect('/basic/student_issue_detail/')
    return render(request,'delete.html')
## DONE WITH ADMIN PAGE ####
