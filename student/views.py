
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Student_table
from .forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# HOME PAGE
def home(request):
    data = {
        'name': "xyz",
        'age': 18,
        'department': "bca"
    }

    marks = [100, 96, 97]

    return render(request, 'home.html', {
        'data': data,
        'marks': marks
    })


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')


# CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# STUDENT REGISTRATION FORM
@login_required(login_url='login')
def student_form(request):

    student = Student_table.objects.filter(
        user=request.user
    ).first()

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            student = form.save(commit=False)
            student.user = request.user
            student.save()

            messages.success(
                request,
                "Student details saved successfully!"
            )

            return redirect('dashboard')

    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {
        'form': form,
        'student': student
    })


# LOGIN PAGE
def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:
            messages.error(
                request,
                "Invalid username or password"
            )

    return render(request, 'login_page.html')


# LOGOUT PAGE
@login_required(login_url='login')
def user_logout(request):

    logout(request)

    return redirect('login')


# USER REGISTRATION
def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully! Please login."
            )

            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form
    })


# STUDENT DASHBOARD
@login_required(login_url='login')
def dashboard(request):

    student = Student_table.objects.filter(
        user=request.user
    ).first()

    return render(request, 'dashboard.html', {
        'student': student
    })

@api_view(['GET', 'POST'])
def student_api(request):

    if request.method == 'GET':
        students = Student_table.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=200)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)