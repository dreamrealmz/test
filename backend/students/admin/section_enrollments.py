from django.contrib import admin
from ..models import SectionEnrollment


@admin.register(SectionEnrollment)
class SectionEnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'section',
        'enrollment_date',
    )
    search_fields = (
        'id',
        'section',
        'enrollment_date',
    )
