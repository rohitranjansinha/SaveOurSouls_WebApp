from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User_Base)
admin.site.register(Hospital_Base)
admin.site.register(Hospital_Location)
admin.site.register(Hospital_OPD)
admin.site.register(Hospital_Wards)
admin.site.register(Results)