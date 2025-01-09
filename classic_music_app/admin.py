from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)


class PropertyShortsInline(admin.StackedInline):
    model = Music


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyShortsInline]

    class Meta:
        model = Compositor

admin.site.register(Compositor, PropertyAdmin)


admin.site.site_header = "DEEP MUSIC"
admin.site.site_title = "DEEP MUSIC"
admin.site.index_title = "DEEP MUSIC"