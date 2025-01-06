from django.contrib import admin
from .models import EquipmentCategory, EquipmentStatus


# Register your models here.
admin.site.register(EquipmentCategory)
admin.site.register(EquipmentStatus)