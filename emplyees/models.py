from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
from django.urls import reverse

class Employees(models.Model):
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=10,choices=[('manager','manager'),('marketing','marketing'),('sales','sales')],default='manager')
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    register = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_details', args=[self.id])