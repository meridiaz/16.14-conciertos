from django.contrib import admin

# Register your models here.

from .models import Grupo, Musico, Concierto

admin.site.register(Grupo)
admin.site.register(Musico)
admin.site.register(Concierto)
