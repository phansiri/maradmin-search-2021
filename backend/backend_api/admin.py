from django.contrib import admin
from .models import Maradmin

@admin.register(Maradmin)
class MaradminAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'date', 'status', 'url_link')
