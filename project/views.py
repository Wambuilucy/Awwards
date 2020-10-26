from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, "employee_registger/employee_list.html")

def projects(request):
    return render(request, "project/projects.html")

def employee_delete(request):
    return