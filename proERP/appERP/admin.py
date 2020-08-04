# Register your models here.
from django.contrib import admin
from .models import Author,Publisher,Language,Genre,BookStore,Course,Student,IssueBook,admin_login
# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(BookStore)

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(admin_login)
admin.site.register(IssueBook)
