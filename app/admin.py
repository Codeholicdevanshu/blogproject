from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Register)
class Adminregister(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','email','phone','password']

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['id','title','text','date']