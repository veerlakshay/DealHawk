from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product" 
        verbose_name_plural = "Products"  

    
class PriceHistory(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.price} on {self.date}"
    
    class Meta:
        verbose_name = "Price History" 
        verbose_name_plural = "Price Histories" 
    
class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15 , blank=True, null=True)
    receive_email_alerts = models.BooleanField(default=True)
    receive_sms_alerts = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "User Profile" 
        verbose_name_plural = "User Profiles"
    