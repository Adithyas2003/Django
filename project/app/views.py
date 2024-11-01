from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("hello")
def fun2(request):
    return HttpResponse("hai")



l=[]
def fun3(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun3)
    else:
        return render(req,'demo.html')
    
def fun4(req):
    return render(req,'about.html')


l=[{'name':'abc','age':'21'},{'name':'cde','age':'12'}]
def display(req):
    a='welcome'
    return render(req,'display.html',{'data':l,'data1':a})


def add_details(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(display)
    else:
        return render(req,'add_details.html')

