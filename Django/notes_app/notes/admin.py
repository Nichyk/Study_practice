from django.contrib import admin

from .models import Notes, Category

admin.site.register(Category)
admin.site.register(Notes)
