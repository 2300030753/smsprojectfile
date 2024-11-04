
from django.urls import path,include
from . import views
app_name='facultyapp'
urlpatterns=[
path('FacultyHomePage/',views.FacultyHomePage,name='FacultyHomePage')
]