from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Display the fields in the admin list view
    list_display = ('name', 'email', 'phone', 'messsage')  # Add 'message' to the list display
    search_fields = ('name', 'email', 'phone')           # Fields to search in admin
    list_filter = ('email',)                             # Add filters for email field
    ordering = ('name',)    