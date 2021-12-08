from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Employees


class EmployeesListView(ListView):
    template_name = "employees/home.html"
    model = Employees


class EmployeesDetailView(DetailView):
    template_name = "employees/employee_details.html"
    model = Employees


class EmployeesCreateView(CreateView):
    template_name = "employees/create.html"
    model = Employees
    fields = ['name','position','start_date','end_date','is_active','register']


class EmployeesUpdateView(UpdateView):
    template_name = "employees/update.html"
    model = Employees
    fields = ['name','position','start_date','end_date','is_active','register']


class EmployeesDeleteView(DeleteView):
    template_name = "employees/delete.html"
    model = Employees
    success_url = reverse_lazy("home")