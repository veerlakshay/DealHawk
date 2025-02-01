from django.core.management.base import BaseCommand
from tracker.models import Product, PriceHistory
from tracker.utils.scraper import scrape_product_price

class Command(BaseCommand):
    help = "Scrapes price for all tracked products"
    
    def handle (self , *args , **kwargs):
        products = Product.objects.all()
        for product in products:
            price = scrape_product_price(product.url)
            if price:
                PriceHistory.objects.create(product=product, price=price)
                self.stdout.write(f"Scrapped price for {product.name} : {price}")
            else:
                self.stdout.write(f"Failed to scrape price for {product.name}")