from django.contrib import admin

from .models import Job,Update,Acheivement,Director,DistrictOfficer, Gallery
# Register your models here.
admin.site.register(Job)
admin.site.register(Update)
admin.site.register(Acheivement)
admin.site.register(Director)
admin.site.register(DistrictOfficer)
admin.site.register(Gallery)