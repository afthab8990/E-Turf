from django.contrib import admin
from .models import*
from Manager_app.models import *
from User_app.models import *

admin.site.register(location)
admin.site.register(turf)
admin.site.register(manager)
admin.site.register(user)
admin.site.register(contact)
admin.site.register(booking)
# Register your models here.
