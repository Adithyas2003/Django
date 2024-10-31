from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("hello")
def fun2(request):
    return HttpResponse("hai")
def fun3(request):
    return render(request,'demo.html')
def fun4(request):
    return render(request,'home.html')
def fun5(request):
    return render(request,'about.html')
def fun6(request):
    return render(request,'contact.html')
