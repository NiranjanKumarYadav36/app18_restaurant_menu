from django.contrib import admin

from restaurent_menu.models import Item


# Register your models here.


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status', )
    search_fields = ('meal', 'description')


admin.site.register(Item, MenuItemAdmin)
