from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


def adminpage(request):
    tdata=turf.objects.all()
    ldata=location.objects.all()
    mdata=manager.objects.all()
    udata=user.objects.all()
    bdata=booking.objects.all()
    unmdata=manager.objects.filter(isapproved=False).count()
    unudata=user.objects.filter(isverified=False).count()

    context = {
        'tdata' : tdata,
        'ldata' : ldata,
        'mdata' : mdata,
        'udata' : udata,
        'bdata' : bdata,
        'unmdata' : unmdata,
        'unudata' : unudata,
    }
    return render(request,'adminpage.html',context)

def addlocations(request):
    return render(request,'addlocations.html')


def insertlocations(request):
    if request.method=='POST':
        city=request.POST['city']
        cityimage=request.FILES['cityimage']
        data=location(city=city,cityimage=cityimage)
        data.save()
    return redirect('adminpage')

def addturfs(request):
    data=location.objects.all()
    mdata=manager.objects.filter(isapproved=True)
    return render(request,'addturfs.html',{'data':data,'mdata':mdata})

def insertturf(request):
    if request.method =='POST':
        turfname=request.POST['turfname']
        capacity=request.POST['capacity']
        rate=request.POST['rate']
        turfimage=request.FILES['turfimage']
        turflocation=request.POST['turflocation']
        managerof=request.POST['managerof']
        data=turf(turfname=turfname,capacity=capacity,rate=rate,turfimage=turfimage,turflocation=turflocation,managerof=managerof)
        data.save()
    return redirect('addturfs')

def editturfs(request,id):
    data=turf.objects.filter(id=id)
    return render(request,'editturfs.html',{'data':data})

def deleteturf(request,id):
    turf.objects.filter(id=id).delete()
    return redirect('viewturfs',category='all')

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
    return redirect('cat_table')

def viewturfs(request,category):
    if(category=="all"):
        data=turf.objects.all()
    else:
        data=turf.objects.filter(turflocation=category)
    # data2=turf.objects.all()
    return render (request,'viewturfs.html',{'data':data})

def viewlocations(request):
    data=location.objects.all()
    return render(request,'viewlocations.html',{'data':data})

def deletelocation(request,id):
    location.objects.filter(id=id).delete()
    return redirect('viewlocations')

def viewmanagers(request):
    data=manager.objects.all()
    return render(request,'viewmanagers.html',{'data':data})

def approvemanager(request,id):
    data=manager.objects.filter(id=id).update(isapproved=True)
    return redirect ('viewmanagers')

def viewcontacts(request):
    data=contact.objects.all()
    return render(request,'viewcontacts.html',{'data':data})

def viewusers(request):
    data=user.objects.all()
    return render(request,'viewusers.html',{'data':data})

def verifyuser(request,id):
    user.objects.filter(id=id).update(isverified=True)
    return redirect('viewusers')

def viewbookings(request):
    data=booking.objects.all()
    return render(request,'viewbookings.html',{'data':data})


# Create your views here.
