from django.contrib import admin
from .models import ArtikelModel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug' , 'published', 'updated'
    ]

admin.site.register(ArtikelModel, ArtikelAdmin)
