from django.contrib import admin
from .models import ApiPost

# Register your models here.

@admin.register(ApiPost)
class ApiPostAdmin(admin.ModelAdmin):
    list_display= ['id','title']

