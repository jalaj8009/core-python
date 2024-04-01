from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello textediting")
     return render(request,"ORS/index.html")
def Welcome(request):
    return render(request,"ORS/Welcome.html")
# def Header(request):
#     return render(request,"ORS/Header.html")

def LoginView(request):
    return render(request,"ORS/LoginView.html")
