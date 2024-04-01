from django.shortcuts import render, redirect
from ..models import developer
from ..service.developerservice import developerservice
from .BaseCtl import BaseCtl




class EmployeedetailCtl(BaseCtl):
    def __init__(self):
        self.form = {}
        self.form["id"] = 0

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["developer_name"] = requestForm["developer_name"]
        self.form["department"] = requestForm["department"]
        self.form["project"] = requestForm["project"]
        self.form["status"] = requestForm["status"]
        self.form["submitting_date"] = requestForm["submitting_date"]
    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.developer_name = self.form["developer_name"]
        obj.department = self.form["department"]
        obj.project = self.form["project"]
        obj.status = self.form["status"]
        obj.submitting_date = self.form["submitting_date"]
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form["id"] = obj.id
        self.form["developer_name"] = obj.developer_name
        self.form["department"] = obj.department
        self.form["project"] = obj.project
        self.form["status"] = obj.status
        self.form["submitting_date"] = obj.submitting_date

    def display(self, request):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request):
        self.request_to_form(request.POST)
        s = self.form_to_model(developer())
        self.get_service().save(s)
        return render(request, self.get_template(), {'form': self.form})

    def edit(self, request, id=0):
        data = self.get_service().get(int(id))
        self.model_to_form(data)
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return developerservice()

    def get_template(self):
        return "Employeeregistration.html"