from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def user_def_form(req):
    if req.method=='POST':
        form1=normal_form(req.POST)
        if form1.is_valid():
            name=form1.cleaned_data['Name']
            age=form1.cleaned_data['user_age']
            email=form1.cleaned_data['email']
            place=form1.cleaned_data['place']
            data=project_user.objects.create(name=name,age=age,email=email,place=place)
            data.save()
            return redirect(user_def_form)
        
    form=normal_form()
    return render(req,'normal_form.html',{'form':form})


def modelform(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
            return redirect(modelform)
    form=model_form()
    return render(req,'model_form.html',{'form':form})
