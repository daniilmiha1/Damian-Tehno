from django.contrib import admin
from .models import Category, Portfolio, Client, Contact
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'cat')}
    list_display = ('name', 'cat', )

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)


