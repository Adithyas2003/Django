from django.shortcuts import render,redirect

# Create your views here.

std=[]
def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        class_name=req.POST['class_name']
        std.append({'roll_no':roll,'name':name,'age':age,'address':address,'class_name':class_name})
        return redirect(home)
    else:
        return render(req,'home.html',{'student':std})
    

def edit_std(req,a):
    data=''
    for i in std:
        if i['roll_no']==a:
            data=i
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        class_name=req.POST['class_name']
        data['roll_no']=roll
        data['name']=name
        data['age']=age
        data['address']=address
        data['class_name']=class_name
        return redirect(home)
    else:
        return render(req,'edit.html',{'data':data})
    
def delete(req,a):
    for i in std:
        if i['roll_no']==a:
            std.remove(i)
    return redirect(home)
