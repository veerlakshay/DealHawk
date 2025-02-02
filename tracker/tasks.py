from celery import shared_task
from .utils.scraper import scrape_product_price
from .models import Product, PriceHistory

@shared_task
def scrape_all_products():
    products = Product.objects.all()
    for product in products:
        price = scrape_product_price(product.url)
        if price:
            # Save the price to PriceHistory
            PriceHistory.objects.create(product=product, price=price)
            print(f"Scraped price for {product.name}: {price}")
        else:
            print(f"Failed to scrape price for {product.name}")