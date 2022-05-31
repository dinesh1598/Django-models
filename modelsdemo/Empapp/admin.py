from django.contrib import admin
from Empapp.models import Employee
 


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    Emp_details=['empNo','empSalary','empName','empAddress']
    



admin.site.register(Employee,EmployeeAdmin)
