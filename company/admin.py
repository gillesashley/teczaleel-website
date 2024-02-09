from django.contrib import admin
from .models import Company, Project, ProjectCoordinator, Sprint, Comment


class ProjectCoordinatorInline(admin.TabularInline):
    model = ProjectCoordinator


class SprintInline(admin.TabularInline):
    model = Sprint


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ProjectInline(admin.TabularInline):
    model = Project
    inlines = [SprintInline]  # Add Sprint inline to Project


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    inlines = [ProjectInline, ProjectCoordinatorInline]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'status', 'progress_percent', 'project_coordinator']
    inlines = [SprintInline]  # Add Sprint inline to Project
    search_fields = ['name', 'company__name']  # Enable searching by project name and company name


class SprintAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'start_date', 'end_date', 'created', 'updated']
    inlines = [CommentInline]  # Add Comment inline to Sprint


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'sprint', 'company', 'created', 'updated']


class ProjectCoordinatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'phone_number', 'company']


# Register models with admin:
admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCoordinator, ProjectCoordinatorAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Comment, CommentAdmin)
