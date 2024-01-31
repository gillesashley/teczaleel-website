from django.contrib import admin

from .models import Company, Project, ProjectCoordinator


# Manage coordinators inline with companies:
class ProjectCoordinatorInline(admin.TabularInline):
    model = ProjectCoordinator


class ProjectInline(admin.TabularInline):
    model = Project


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    inlines = [ProjectInline, ProjectCoordinatorInline]  # Add coordinator inline


# No inlines needed for ProjectAdmin:
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'status', 'progress_percent']  # Add useful fields


class ProjectCoordinatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company']


# Register models with admin:
admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCoordinator, ProjectCoordinatorAdmin)  # Keep separate registration
