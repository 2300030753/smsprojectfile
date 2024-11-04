from django.shortcuts import render

def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')

