from django.contrib import admin
from .models import Category,course,Lesson,Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','name']
    search_fields = ['name']
    list_filter = ['id','name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(course)
admin.site.register(Lesson)
admin.site.register(Tag)

# Register your models here.

