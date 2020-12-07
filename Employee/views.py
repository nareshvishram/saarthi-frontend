from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def Home(request):
    dict={}
    if request.method=="POST":
        data=request.POST
        emp_name=data["emp_name"]
        emp_id=data["emp_id"]
        emp_dept = data["emp_dept"]
        emp_email = data["emp_email"]
        emp_doj = data["emp_doj"]
        Employee.objects.create(eid=emp_id,name=emp_name,dept=emp_dept,email=emp_email,doj=emp_doj)
        return redirect("home")
    all_employee = Employee.objects.all().order_by("-id")
    dict = {"all_employee": all_employee}
    return render(request,"index.html",dict)

def Remove(request,emp_id):
    emp_data=Employee.objects.get(id=emp_id)
    emp_data.delete()
    return redirect("home")
