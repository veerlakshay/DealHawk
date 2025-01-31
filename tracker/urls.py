from django.urls import path
from . import views

urlpatterns = [
    # Product URLs
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    # PriceHistory URLs
    path('price-history/', views.PriceHistoryList.as_view(), name='pricehistory-list'),
    path('price-history/<int:pk>/', views.PriceHistoryDetail.as_view(), name='pricehistory-detail'),

    # UserProfile URLs
    path('user-profiles/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('user-profiles/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail'),
]