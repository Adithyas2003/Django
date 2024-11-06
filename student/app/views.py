from django.shortcuts import render,redirect
from .models import *

# Create your views here.

std=[]
def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        class_name=req.POST['class_name']
        # std.append({'roll_no':roll,'name':name,'age':age,'address':address,'class_name':class_name})
        data=Student.objects.create(roll_no=roll,name=name,age=age,address=address,class_name=class_name)
        data.save()
        return redirect(home)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'student':data})
    

def edit_std(req,id):
   
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        class_name=req.POST['class_name']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,address=address,class_name=class_name)
        return redirect(home)
    else:
        data=Student.objects.get(pk=id)
        return render(req,'edit.html',{'data':data})
    
def delete(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(home)
