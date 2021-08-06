from django.contrib import admin
from .models import *


class GymProfileInline(admin.TabularInline):
    model = GymProfile.locations.through
    model._meta.verbose_name_plural = "Локации"
    model._meta.verbose_name = 'Локация'
    sortable_field_name = 'city'
    extra = 1


class RaitingInline(admin.StackedInline):
    model = Raiting


class GymProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = (GymProfileInline, RaitingInline)
    fieldsets = [
        ('', {
            'fields': ('name', 'address', 'general_comment')
        })
    ]


admin.site.register(GymProfile, GymProfileAdmin)
admin.site.register(City)
admin.site.register(Location)
