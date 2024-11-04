import calendar

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
import random
import string
import datetime
from datetime import datetime
from datetime import timedelta
from .models import Task
from .forms import TaskForm
def ProjectHomePage(request):
    return render(request,'adminapp/ProjectHomePage.html')
def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpagelogic(request):
    if request.method == "POST":
        user_input=request.POST['user_input']
        print(f'User input: {user_input}')
    a1={'user_input': user_input}
    return render(request,'adminapp/printer.html',a1)
def exceptionpagecall(request):
    return render(request, 'adminapp/print_to_console.html')



def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        try:
            result = process_user_input(user_input)
            return render(request, 'adminapp/print_to_console.html', {'result': result})
        except Exception as e:
            return render(request, 'adminapp/print_to_console.html', {'error': str(e)})
    return render(request, 'adminapp/print_to_console.html')
def process_user_input(user_input):
    try:
        num = int(user_input)
        result = 10 / num
        return result
    except ZeroDivisionError:
        raise Exception('Cannot divide by zero.')
    except ValueError:
        raise Exception('Invalid input. Please enter a valid number.')
def randompagecall(request):
    return render(request,'adminapp/randomexample.html')
def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
        a1={'ran':ran}
        return render(request,'adminapp/randomexample.html',a1)


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'
    return render(request, 'adminapp/calcutions.html', {'result': result})
def calculatorpagecall(request):
    return render(request,'adminapp/calcutions.html')
def datetimepagecall(request):
    return render(request,'adminapp/datetimepage.html')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html',
                      {'form': form, 'tasks': tasks})

def datetimepagelogic(request):
    ran = None
    ran1 = None
    ran3 = None
    number1 = None

    if request.method == "POST":
        try:
            number1 = int(request.POST['date1'])
            x = datetime.now()
            ran = x + timedelta(days=number1)
            ran1 = ran.year
            ran2 = calendar.isleap(ran1)
            ran3 = "Leap year" if ran2 else "Not a leap year"
        except (ValueError, KeyError):
            # Handle the case where 'date1' is not a valid integer or not provided
            ran3 = "Invalid input"

    a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    return render(request, 'adminapp/datetimepage.html', a1)


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')



def UserLoginPageCall(request):
    return render(request, 'adminapp/loginpage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from .forms import StudentForm
from .models import StudentList

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})