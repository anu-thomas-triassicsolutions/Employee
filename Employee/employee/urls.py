from django.urls import path
from .import views

urlpatterns = [
    path('employee_data/', views.employee_data, name='employee_data'),  # Path for Home

]