from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='home'),
    path('students/student_form/', views.student_list, name='student_list'),
]