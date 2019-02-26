from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolInformation(TemplateView):
    template_name = 'SchoolInformation.html'

class StudentInformation(TemplateView):
    template_name = 'StudentInformation.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student

class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = models.School
    template_name ="app1/school_detail.html"

class StudentDetailView(DetailView):
    context_object_name = 'student'
    model = models.Student
    template_name ="app1/student_detail.html"

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class StudentCreateView(CreateView):
    fields =('name','age','school')
    model =models.Student

class SchoolUpdateView(UpdateView):
    fields = ('name','principal','location')
    model = models.School

class StudentUpdateView(UpdateView):
    fields = ('name','age','school')
    model = models.Student

class SchoolDeleteView(DeleteView):
    model =models.School
    success_url=reverse_lazy('app1:school_list')

class StudentDeleteView(DeleteView):
    model =models.Student
    success_url=reverse_lazy('app1:student_list')
