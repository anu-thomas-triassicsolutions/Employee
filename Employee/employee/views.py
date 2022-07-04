from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from employee.models import Employee
from. serializer import EmployeeSerializer


def employee_data(request):
    task2 = Employee.objects.all()  # call all objects in Employee
    if request.method == "POST":  # Take data from user
        employee = request.POST['employee']
        designation = request.POST['designation']
        emp = Employee(name=employee, designation=designation)  # Add date to Employee
        emp.save()  # Save data to Employee
    return render(request, 'employee.html', {'emp': task2})  # Passing Objects to html page


class EmployeeList(ListAPIView):
    queryset = Employee.objects.filter(designation='HR')  # filter using designation
    serializer_class = EmployeeSerializer  # importing JSoN file
    filter_backends = (DjangoFilterBackend, OrderingFilter)  # Ordering
    # filter_fields = ('name')
    ordering_fields = ('designation', 'name')
    ordering = 'name'
