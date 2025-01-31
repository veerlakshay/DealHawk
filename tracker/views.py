from rest_framework import generics
from .models import Product, PriceHistory, UserProfile
from .serializers import ProductSerializer, PriceHistorySerializer, UserProfileSerializer

# Product Views
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# PriceHistory Views
class PriceHistoryList(generics.ListCreateAPIView):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

class PriceHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

# UserProfile Views
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer