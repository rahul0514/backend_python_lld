from django.contrib import admin
from ecomdemo.models import User, Products


# admin.site.register(User)
# admin.site.register(Products)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email']
    list_display = ['id', 'username', 'name']
    search_fields = ['id', 'name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = [ 'name', 'description', 'price', 'stock']
    list_display = ['id', 'name', 'price']
    search_fields = ['id']

