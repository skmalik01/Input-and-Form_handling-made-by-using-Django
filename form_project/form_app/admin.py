from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'uploaded_file')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
