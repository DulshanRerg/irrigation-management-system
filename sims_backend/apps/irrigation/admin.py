from django.contrib import admin
from .models import IrrigationZone, IrrigationSchedule, AutomatedIrrigation

# Register your models here.

admin.site.register(IrrigationZone)
admin.site.register(IrrigationSchedule)
admin.site.register(AutomatedIrrigation)
