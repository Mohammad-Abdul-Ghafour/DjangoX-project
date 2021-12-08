from django.contrib import admin
from .models import Employees
# Register your models here.

@admin.register(Employees)
class EmployeesTable(admin.ModelAdmin):
    list_display = ['name','position','is_active']