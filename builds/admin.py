from django.contrib import admin
from .models import Build
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = (
        'build_title',
        'featured_image',
        'slug',
        'image',
        'build_time',
        'build_type',
        'set_number',
        'difficulty_rating',
        'content',
        'created_on'
    )
    list_filter = ('build_type',)
