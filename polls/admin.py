from django.contrib import admin
from .models import Entity
from .models import Info

# Register your models here.
admin.site.register(Entity)
admin.site.register(Info)