from django.contrib import admin
from apps.maps import models
# Register your models here.
admin.site.register(models.Stop)
admin.site.register(models.Route)
# we want to see this model in the admin page, above code does this