from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display  = [
        'reference_number',
        'issue_type',
        'address',
        'language',
        'mode',
        'status',
        'submitted_at'
    ]
    list_editable = ['status']
    list_filter   = ['status', 'issue_type', 'language', 'mode']
    search_fields = ['reference_number', 'address', 'phone_number']
    readonly_fields = ['reference_number', 'submitted_at']
    fieldsets = (
        ('Report Info', {
            'fields': ('reference_number', 'issue_type', 'address', 'description', 'submitted_at')
        }),
        ('User Info', {
            'fields': ('language', 'mode', 'phone_number')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )
