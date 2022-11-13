from django.contrib import admin
from .models import Entry
# Register your models here.



@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display=['title','author']
    search_fields =['title']
    list_filter = ['created_at','title']
     