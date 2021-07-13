from django.contrib import admin
from content.models import *


class CategoryAdmin(admin.ModelAdmin):
    def show_description(self, obj):
        return obj.description[:30]

    def make_visible(self, request, queryset):
        queryset.update(is_view=True)

    def make_unvisible(self, request, queryset):
        queryset.update(is_view=False)

    list_display = ['name', 'is_view', 'show_description', 'create_date']
    ordering = ['name', 'is_view', 'create_date']
    actions = [make_visible, make_unvisible]
    make_visible.short_description = 'Отключить отображение выбранных элементов'
    make_unvisible.short_description = 'Включить отображение выбранных элементов'


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'create_date']
    ordering = ['name', 'category', 'create_date']
    fieldsets = [
        ('Information', {
            'fields': ('name', 'category')
        }),
        ('Добавить фото или видео <a href=""> </a>', {
            'fields': ('text', )
        })
    ]


admin.site.register(Exercise, PublicationAdmin)
admin.site.register(Product, PublicationAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(ExerciseCategory, CategoryAdmin)
admin.site.register(ButtonOneText)
