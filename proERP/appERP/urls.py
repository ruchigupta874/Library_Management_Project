from django.urls import path
from . import views

app_name = 'appERP'

urlpatterns = [
    path('list/',views.AuthorListView.as_view(),name='list'),
    #path('list/<int:pk>/',views.BookDetailView.as_view(),name='list'),
    path('create/',views.AuthorCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.AuthorUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='delete'),

    path('pub_list/',views.PublisherListView.as_view(),name='pub_list'),
    path('pub_create/',views.PublisherCreateView.as_view(),name='pub_create'),
    path('pub_update/<int:pk>/',views.PublisherUpdateView.as_view(),name='pub_update'),
    path('pub_delete/<int:pk>/', views.PublisherDeleteView.as_view(), name='pub_delete'),

    path('lan_list/', views.LanguageListView.as_view(), name='lan_list'),
    path('lan_create/', views.LanguageCreateView.as_view(), name='lan_create'),
    path('lan_update/<int:pk>/', views.LanguageUpdateView.as_view(), name='lan_update'),
    path('lan_delete/<int:pk>/', views.LanguageDeleteView.as_view(), name='lan_delete'),

    path('gen_list/', views.GenreListView.as_view(), name='gen_list'),
    path('gen_create/', views.GenreCreateView.as_view(), name='gen_create'),
    path('gen_update/<int:pk>/', views.GenreUpdateView.as_view(), name='gen_update'),
    path('gen_delete/<int:pk>/', views.GenreDeleteView.as_view(), name='gen_delete'),

    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),

    path('stu_list/', views.StudentListView.as_view(), name='stu_list'),
    path('stu_create/',views.StudentCreateView.as_view(),name='stu_create'),
    path('stu_update/<str:pk>/',views.StudentUpdateView.as_view(),name='stu_update'),
    path('stu_delete/<str:pk>/', views.StudentDeleteView.as_view(), name='stu_delete'),

    path('course_list/', views.CourseListView.as_view(), name='course_list'),
    path('course_create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course_update/<str:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course_delete/<str:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),

    path('issue_list/', views.IssueBookListView.as_view(), name='issue_list'),
    #path('issue_create/', views.IssueBookCreateView.as_view(), name='issue_create'),
    path('issue_create/',views.issue_view,name='issue_create'),
    path('student_issue_detail/',views.StudentIssueDetail,name='student_issue_detail'),
    #path('issue_delete/<str:pk>',views.IssueBookDeleteView.as_view(),name='issue_delete'),

    path('home/',views.homeView.as_view(),name='home'),

    path('stu_home/',views.StudentHomeView.as_view(),name='stu_home'),
    path('stu_search/',views.form_view,name='stu_search'),
   # path('stu_login/',views.login_student,name='stu_login'),

    path('student_issue_detail/',views.StudentIssueDetail,name='student_issue_detail'),
    path('issueDelete/<str:pk>',views.IssueDelete,name='issueDelete'), # for returning  book
   # path('stu_fine',views.fine_student,name='stu_fine'),
    path('studentdetail/', views.student_issue, name = 'student_detail')

]
