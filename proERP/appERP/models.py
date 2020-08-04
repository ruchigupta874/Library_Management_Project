from django.db import models
from django.urls import reverse
# NEVER EVER IMPORT VIEWS IN MODELS ERROR CIRCULAR IMPORT ERROR

# Book Realted models here.
from django.utils import timezone
import datetime

class Author(models.Model):
    author_name=models.CharField(max_length=200)
    author_description=models.CharField(max_length=200)

    def __str__(self):
        return self.author_name

    def get_absolute_url(self):
        return reverse("appERP:list")

class Publisher(models.Model):
    publisher_name=models.CharField(max_length=200)
    publisher_description=models.CharField(max_length=200)

    def __str__(self):
        return self.publisher_name

    def get_absolute_url(self):
        return reverse("appERP:pub_list")

class Language(models.Model):
    language_name=models.CharField(max_length=200)
    language_description=models.CharField(max_length=200)

    def __str__(self):
        return self.language_name

    def get_absolute_url(self):
        return reverse("appERP:lan_list")

class Genre(models.Model):
    genre_name=models.CharField(max_length=200)
    genre_description=models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name
    def get_absolute_url(self):
        return reverse("appERP:gen_list")

class BookStore(models.Model):
    book_name=models.CharField(max_length=200)
    book_author=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    book_language=models.ForeignKey(Language,on_delete=models.CASCADE)
    book_genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    book_ISBN=models.CharField(max_length=200)
    book_copies=models.PositiveIntegerField()
    book_price=models.PositiveIntegerField()
    book_description=models.CharField(max_length=200)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse("appERP:book_list")

class Course(models.Model):
    course_name=models.CharField(max_length=200)
    course_description=models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("appERP:course_list")

class Student(models.Model):
    student_rollno=models.CharField(max_length=200,primary_key=True,unique=True)
    student_name=models.CharField(max_length=200)
    student_email=models.EmailField(max_length=200)
    student_phone_number= models.CharField(max_length=12)
    student_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student_DOB=models.CharField(max_length=200)
    student_admissiondate=models.CharField(max_length=200)
    student_address=models.CharField(max_length=200)
    #student_profile_pic = models.ImageField(upload_to='pictures', blank=True)
    def __str__(self):
        return self.student_rollno

    def get_absolute_url(self):
        return reverse("appERP:stu_list")


class IssueBook(models.Model):
    issueRollno=models.ForeignKey(Student,on_delete=models.CASCADE)
    issueBookName=models.ForeignKey(BookStore,on_delete=models.CASCADE)
    issue_date=models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now()+datetime.timedelta(10))
    fine = models.PositiveIntegerField(blank=True,default=0)

    def __str__(self):
        return self.issueBookName.book_name

    def get_absolute_url(self):
        return reverse("appERP:issue_list")


#### ADMIN SIGNUP AND LOGIN MODELS
class admin_login(models.Model):
    l_rollno = models.ForeignKey(Student, on_delete=models.CASCADE)
    l_password = models.CharField(max_length=200,default='ncuindia')

    def __str__(self):
        return self.l_rollno.student_rollno




