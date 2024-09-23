from django.urls import path
from .import views
urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('newreg',views.newreg,name='newreg'),
    path('sessionlogin',views.sessionlogin,name='sessionlogin'),
    path('managerhome',views.managerhome,name='managerhome'),
    path('yourturfs',views.yourturfs,name='yourturfs'),
    path('editturfmanager<int:id>',views.editturf,name='editturfmanager'),
    path('updateturfmanager<int:id>',views.updateturf,name='updateturfmanager'),
    path('allturfs',views.allturfs,name='allturfs'),
    path('endsession',views.endsession,name='endsession'),
    path('managebookings',views.managebookings,name='managebookings'),
    path('updatebooking<int:id>',views.updatebooking,name='updatebooking'),
    path('deletebooking<int:id>',views.deletebooking,name='deletebooking'),

]
