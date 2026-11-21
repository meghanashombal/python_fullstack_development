
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import StudentForm
from .models import students, Product


# Home Page
def home(request):
    return render(request, 'students/home.html')


# Registration Page
def register(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/register.html',
        {'form': form}
    )


# Student Registration Form
def student_form(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/register.html',
        {'form': form}
    )


# Student List
def student_list(request):

    all_students = students.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': all_students}
    )


# Login Page
def login_page(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

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

            return render(
                request,
                'students/login.html',
                {
                    'error': 'Invalid username or password!'
                }
            )

    return render(request, 'students/login.html')


# Dashboard
@login_required(login_url='login')
def dashboard(request):

    return render(
        request,
        'students/dashboard.html'
    )


# Logout
def logout_page(request):

    if request.method == 'POST':
        logout(request)

    return redirect('home')


# Products Page
def products(request):

    all_products = Product.objects.all()

    return render(
        request,
        'students/products.html',
        {'products': all_products}
    )
