from django.contrib import admin
from dictribution.models import Dictribution


class DictributionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_sended', 'send_date_time']
    ordering = ['name', 'is_sended', 'send_date_time']


admin.site.register(Dictribution, DictributionAdmin)
