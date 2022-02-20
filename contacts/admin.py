from re import search
from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'surname', 
        'phone', 
        'email', 
        'creation_date', 
        'category',
        'show',
    )
    list_display_links = ('id', 'name', 'surname')
    list_per_page = 10
    search_fields = ('name', 'surname', 'phone', 'email', 'description')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)