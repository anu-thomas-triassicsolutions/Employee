from employee import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeList.as_view()),
    path('', include('employee.urls')),
    path('', include('authentication.urls')),

]
