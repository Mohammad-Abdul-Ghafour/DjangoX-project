from django.urls import path
from .views import EmployeesCreateView,EmployeesDeleteView,EmployeesDetailView,EmployeesListView,EmployeesUpdateView

urlpatterns = [
    path('', EmployeesListView.as_view(), name='home'),
    path('<int:pk>/', EmployeesDetailView.as_view(), name='employee_details'),
    path('create/', EmployeesCreateView.as_view(), name='create_employee'),
    path('update/<int:pk>/', EmployeesUpdateView.as_view(), name='update_employee'),
    path('delete/<int:pk>/', EmployeesDeleteView.as_view(), name='delete_employee'),
]