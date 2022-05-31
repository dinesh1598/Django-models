from django.shortcuts import render
from Empapp.models import Employee 
#employee is a class name


def empdetails(request):
    emp_data=Employee.objects.all()
    #the above line takes all the employee objects from model
    emp_dic={'emp_list':emp_data}
    #the above  line send the data in dictionary format for render it is complesary
    #we must send the data in dictionary format
    return render(request,'Empapp/employee.html',context=emp_dic)

# Create your views here.
