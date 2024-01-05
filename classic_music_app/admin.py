from django.contrib import admin
from .models import *

class PropertyShortsInline(admin.StackedInline):
    model = Music


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyShortsInline]

    class Meta:
        model = Compositor

admin.site.register(Compositor, PropertyAdmin)