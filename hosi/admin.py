from django.contrib import admin

from hosi.models import Appointment, Query, Newsletter

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Query)
admin.site.register(Newsletter)