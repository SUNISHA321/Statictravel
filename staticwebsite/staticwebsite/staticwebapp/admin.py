from django.contrib import admin

# Register your models here.
from . models import Place,Team

admin.site.register(Place)
admin.site.register(Team)
