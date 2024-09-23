from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from Admin_app.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


def loginpage(request):
    return render(request,'loginpage.html')

def registeruser(request):
    return render (request,'registeruser.html')

def newreg(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        password=request.POST['password']
        data=manager(name=name,username=username,email=email,phonenumber=phonenumber,password=password)
        data.save()
    return redirect('loginpage')

def sessionlogin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if manager.objects.filter(username=username,password=password,isapproved=True).exists():
           data = manager.objects.filter(username=username,password=password).values('name','phonenumber','email','isassigned').first()
           request.session['name_u'] = data['name']
           request.session['phonenumber_u'] = data['phonenumber'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           request.session['isassigned_u'] = data['isassigned']
           return redirect('managerhome') 
        else:
            return render(request,'loginpage.html',{'msg':'invalid user credentials ot waiting for approval'})
    else:
        return redirect('loginpage')
    
def managerhome(request):
    tdata=turf.objects.all()
    username=request.session.get('username_u')
    ytdata=turf.objects.filter(managerof=username)
    bdata=booking.objects.all()
    data=request.session.get('data',[])
    return render(request,'managerhome.html',{'data':data,'tdata':tdata,'ytdata':ytdata,'bdata':bdata})

def allturfs(request):
    data=turf.objects.all()
    return render(request,'allturfs.html',{'data':data})

def yourturfs(request):
    username=request.session.get('username_u')
    data=turf.objects.filter(managerof=username)
    return render(request,'yourturfs.html',{'data':data})

def editturf(request,id):
    data=turf.objects.filter(id=id)
    return render(request,'editturf.html',{'data':data})

def updateturf(request,id):
    if request.method == 'POST':
        turfname = request.POST.get('turfname')
        capacity = request.POST.get('capacity')
        rate = request.POST.get('rate')
        try:
            img_c = request.FILES['turfimage']
            fs = FileSystemStorage()
            turfimage = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            turfimage = turf.objects.get(id=id).turfimage
        turf.objects.filter(id=id).update(turfname=turfname,capacity=capacity,rate=rate,turfimage=turfimage)
    return redirect('managerhome')

def endsession(request):
    del request.session['username_u']
    del request.session['password_u']
    return redirect('loginpage')

def managebookings(request):
    data = booking.objects.filter()
    return render(request,'managebookings.html',{'data':data})

def updatebooking(request,id):
    booking.objects.filter(id=id).update(booked='booked')
    return redirect('managebookings')

def deletebooking(request,id):
    booking.objects.filter(id=id).delete()
    return redirect('managebookings')
# Create your views here.
