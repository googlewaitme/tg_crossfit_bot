from django.contrib import admin
from content.models import *


class CategoryAdmin(admin.ModelAdmin):
    def show_description(self, obj):
        return obj.description[:30]

    def make_viewed(self, request, queryset):
        queryset.update(is_view=True)

    def make_desviewed(self, request, queryset):
        queryset.update(is_view=False)

    list_display = ['name', 'is_view', 'show_description']
    ordering = ['name', 'is_view']
    actions = [make_viewed, make_desviewed]
    make_desviewed.short_description = 'Отключить отображение выбранных элементов'
    make_viewed.short_description = 'Включить отображение выбранных элементов'


admin.site.register(Exercise)
admin.site.register(Product)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(ExerciseCategory, CategoryAdmin)
admin.site.register(ButtonOneText)
