from django.urls import path
from .import views
urlpatterns = [
    path('',views.adminpage,name='adminpage'),
    path('addlocations',views.addlocations,name='addlocations'),
    path('insertlocations',views.insertlocations,name='insertlocations'),
    path('viewlocations',views.viewlocations,name='viewlocations'),
    path('deletelocation<int:id>',views.deletelocation,name='deletelocation'),
    path('addturfs',views.addturfs,name='addturfs'),
    path('insertturf',views.insertturf,name='insertturf'),
    path('viewturfs<str:category>',views.viewturfs,name='viewturfs'),
    path('updateturf<int:id>',views.updateturf,name='updateturf'),
    # path('addslots<int:id>',views.addslots,name='addslots'),
    # path('viewslots<int:id>',views.viewslots,name='viewslots'),
    path('deleteturf<int:id>',views.deleteturf,name='deleteturf'),
    path('editturfs<int:id>',views.editturfs,name='editturfs'),
    path('viewmanagers',views.viewmanagers,name='viewmanagers'),
    path('approvemanager<int:id>',views.approvemanager,name='approvemanager'),
    path('viewcontatcs',views.viewcontacts,name='viewcontacts'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('verifyuser<int:id>',views.verifyuser,name='verifyuser'),
    path('viewbookings',views.viewbookings,name='viewbookings')
]
