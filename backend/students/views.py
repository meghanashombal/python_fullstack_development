from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import students

def student_form(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form})


def student_list(request):
    student_data = students.objects.all()
    return render(request, 'students/student_list.html', {'students': student_data})