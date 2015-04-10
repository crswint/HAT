from django.contrib import admin
from apps.maps import models
# Register your models here.
admin.site.register(models.Stop)
admin.site.register(models.Route)
admin.site.register(models.R1NStops)
admin.site.register(models.R1SStops)
admin.site.register(models.R2Stops)
admin.site.register(models.R3Stops)
admin.site.register(models.R4Stops)
admin.site.register(models.R5AStops)
admin.site.register(models.R5BStops)
admin.site.register(models.R6Stops)
# we want to see this model in the admin page, above code does this