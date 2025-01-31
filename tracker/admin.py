from django.contrib import admin
from .models import Product, PriceHistory, UserProfile

# Customize Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')  # Columns to display
    search_fields = ('name', 'url')  # Add a search bar
    list_filter = ('created_at', 'updated_at')  # Add filters

# Customize PriceHistory Admin
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'date')  # Columns to display
    list_filter = ('date', 'product')  # Add filters

# Customize UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'receive_email_alerts', 'receive_sms_alerts')  # Columns to display
    search_fields = ('user__username', 'phone_number')  # Add a search bar

# Register models with custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(PriceHistory, PriceHistoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)