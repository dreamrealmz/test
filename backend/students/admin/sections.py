from django.contrib import admin
from ..models import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
