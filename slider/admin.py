from django.contrib import admin
from .models import SliderImage

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
