from django.contrib import admin
from .models import Project, ProjectImage, Category, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3          # Default 3 boş sahə göstərir
    fields = ['image', 'caption', 'order']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'order', 'created_at']
    list_filter = ['status', 'is_featured', 'category']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_featured', 'status']
    ordering = ['order', '-created_at']
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Əsas Məlumat', {
            'fields': ('title', 'description', 'short_description', 'category')
        }),
        ('Video', {
            'fields': ('video_url', 'video_file'),
            'description': 'Şəkillər aşağıdakı "Proyekt Şəkilləri" bölməsindən əlavə edilir'
        }),
        ('Linklər', {
            'fields': ('project_url', 'github_url')
        }),
        ('Digər', {
            'fields': ('technologies', 'status', 'is_featured', 'order')
        }),
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_editable = ['order']
    ordering = ['project', 'order']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email']