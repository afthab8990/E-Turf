from django.shortcuts import render,redirect
from django.http import HttpResponse
from Admin_app.models import *
from .models import *

def userhome(request):
    data=turf.objects.filter(isbooked=False)
    data2=location.objects.all()
    return render(request,'userhome.html',{'data':data,'data2':data2})

def userlogin(request):
    return render(request,'userlogin.html')

def userregister(request):
    return render(request,'userregister.html')

def insertuser(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        data=user(name=name,username=username,email=email,phonenumber=phonenumber,password=password)
        data.save()
    return redirect ('userlogin')

def usersession(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if user.objects.filter(username=username,password=password,isverified = True).exists():
            data=user.objects.filter(username=username,password=password).values('name','email','phonenumber','id').first()
            request.session['name_u']=data['name']
            request.session['email_u']=data['email']
            request.session['u_id']=data['id']
            request.session['phonenumber_u']=data['phonenumber']
            request.session['username_u']=username
            request.session['password_u']=password
            return redirect('userhome')
        else:
            return render(request, 'userlogin.html',{'msg':'Wrong credentials or not verified'})
    else:
        return redirect('userlogin')
    
def deletesession(request):
    del request.session['username_u']
    del request.session['email_u']
    del request.session['u_id']
    del request.session['password_u']
    del request.session['phonenumber_u']
    return redirect('userlogin')

def usercontact(request):
    return render (request,'usercontact.html')

def insertmessage(request):
    if request.method=='POST':
        name=request.POST['name']
        message=request.POST['message']
        data=contact(name=name,message=message)
        data.save()
    return redirect('userhome')

def locationsort(request):
    data=location.objects.all()
    return render(request,'locationsort.html',{'data':data})

def turfsort(request,category):
    if (category=="all"):
        data=turf.objects.all()
    else:
        data=turf.objects.filter(turflocation=category)
    return render(request, 'turfsort.html',{'data':data})

def turfbooking(request,id):
    data=turf.objects.filter(id=id)
    return render(request,'turfbooking.html',{'data':data})

def bookslot(request,id):
    if request.method== "POST":
        username=request.session.get('u_id')
        bslot=request.POST['bslot']
        bturf=turf.objects.get(id=id)
        data=booking(buser=user.objects.get(id=username),bturf=bturf,bslot=bslot)
        if booking.objects.filter(bturf=bturf,bslot=bslot,booked='booked').exists():
            return render(request,'turfsort.html',{'Message':'The booking already exists'})
        else:
            data.save()
            
    return redirect('userhome')

def bookinghistory(request,id):
    username=request.session.get('username_u')
    if username:
        data=booking.objects.filter(buser__username=username)
        return render (request,'bookinghistory.html',{'data':data})
    else:
        return redirect('userhome')


# Create your views here.
