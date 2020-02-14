from django.contrib import admin
from .models import Navigation, Vehicle

# Register your models here.

class NavAdmin(admin.ModelAdmin):

    list_display = ['latitude', 'longitude', 'vehicle_id', 'vehicle', 'datetime']
    list_display_links = ['latitude', 'longitude', 'vehicle']
    list_filter = ['datetime']

class VehicleAdmin(admin.ModelAdmin):

    list_display = ['id', 'plate']
    list_display_links = ['plate']

    class Meta:
        model = Navigation

admin.site.register(Navigation, NavAdmin)
admin.site.register(Vehicle, VehicleAdmin)