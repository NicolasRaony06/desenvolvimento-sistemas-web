from django.contrib import admin
from .models import Event, Activity, Report

# Register your models here.
class ActivityInline(admin.TabularInline):
    model = Activity

class ReportInline(admin.TabularInline):
    model = Report

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'location']
    list_filter = ['location__name', 'categories']
    search_fields = ['title']
    inlines = [ActivityInline, ReportInline]

admin.site.register(Report)