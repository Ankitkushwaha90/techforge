from django.contrib import admin
from .models import Course, Module, Content

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1
    fields = ('title', 'description', 'code', 'code_language', 'order')

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    fields = ('title', 'description', 'order')
    show_change_link = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'created_at', 'updated_at')
    list_filter = ('course',)
    inlines = [ContentInline]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'code_language', 'order', 'created_at', 'updated_at')
    list_filter = ('module__course', 'code_language')
    search_fields = ('title', 'description', 'code')
