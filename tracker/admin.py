from django.contrib import admin
from .models import Product, PriceHistory, UserProfile

# Register your models here
admin.site.register(Product)
admin.site.register(PriceHistory)
admin.site.register(UserProfile)
