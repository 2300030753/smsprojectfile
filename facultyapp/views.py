from django.shortcuts import render

# Create your views here.
def FacultyHomePage(request):
    return render(request,'facultyapp/FacultyHomePage.html')

