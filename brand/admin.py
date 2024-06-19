from django.contrib import admin
from . import models
# admin.site.register(models.BrandModel)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brand_name',)}
    list_display = ['brand_name','slug']

admin.site.register(models.BrandModel,BrandAdmin)