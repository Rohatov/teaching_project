from django.contrib import admin
from home.models import LessonPlans, Achievements, Videos, Photos, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # list_filter = ('category_id',)

@admin.register(LessonPlans)
class LessonPlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
    search_fields = ('title',)
    list_filter = ('title','category_id')

@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'doc')
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'video')
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)
    list_filter = ('title',)
