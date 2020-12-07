from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import requests as req
import json
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


def jprint(obj):
    # create a formatted string of the Python JSON object

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

class BearerAuth(req.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def api(request):
    endpoint="https://f0ztti2nsk.execute-api.ap-south-1.amazonaws.com/v1/consignment/fetch"
    BearerToken="tTU3gFVUdP"
    body={"email":"mayankmittal@intugine.com"}
    param="mayank"
    header={
          "Authorization":'Bearer tTU3gFVUdP',
            }

    try:
       data=req.post(endpoint,auth =('email', 'mayankmittal@intugine.com'),headers=header,verify=True)
       print(data.text)
    except req.exceptions.ConnectionError:
        req.status_code = "Connection refused"

    return HttpResponse("Passed")