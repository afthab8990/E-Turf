from django.urls import path
from .import views
urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('userhome',views.userhome,name='userhome'),
    path('userregister',views.userregister,name='userregister'),
    path('insertuser',views.insertuser,name='insertuser'),
    path('usersession',views.usersession,name='usersession'),
    path('deletesession',views.deletesession,name='deletesession'),
    path('usercontact',views.usercontact,name='usercontact'),
    path('insertmessage',views.insertmessage,name='insertmessage'),
    path('locationsort',views.locationsort,name='locationsort'),
    path('turfsort<str:category>',views.turfsort,name='turfsort'),
    path('turfbooking<int:id>',views.turfbooking,name='turfbooking'),
    path('bookslot<int:id>',views.bookslot,name='bookslot'),
    path('bookinghistory<str:id>',views.bookinghistory,name='bookinghistory')
]
