from django.contrib import admin
from base import models
# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

class DestinationAdmin(admin.ModelAdmin):
    list_display = [
        "spot_Title",
    ]

class PackagesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
admin.site.register(models.district,DistrictAdmin)
admin.site.register(models.popular_Destination,DestinationAdmin)
admin.site.register(models.packages ,PackagesAdmin)