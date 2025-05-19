from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    # Product List endpoints
    path("", ProductListAPIView.as_view(), name="product-list"),
    path("<int:pk>/", ProductRetrieveAPIView.as_view(), name="product-retrieve"),
    
    # Product CRUD endpoints
    path("create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("<int:pk>/delete/", ProductDeleteAPIView.as_view(), name="product-delete"),
    
    # Brand CRUD endpoints
    path("brands/", BrandListAPIView.as_view(), name="brand-list"),
    path("brands/<int:pk>/", BrandRetrieveAPIView.as_view(), name="brand-retrieve"),
    path("brands/create/", BrandCreateAPIView.as_view(), name="brand-create"),
    path("brands/<int:pk>/update/", BrandUpdateAPIView.as_view(), name="brand-update"),
    path("brands/<int:pk>/delete/", BrandDeleteAPIView.as_view(), name="brand-delete"),
    
    # Color CRUD endpoints
    path("colors/", ColorListAPIView.as_view(), name="color-list"),
    path("colors/<int:pk>/", ColorRetrieveAPIView.as_view(), name="color-retrieve"),
    path("colors/create/", ColorCreateAPIView.as_view(), name="color-create"),
    path("colors/<int:pk>/update/", ColorUpdateAPIView.as_view(), name="color-update"),
    path("colors/<int:pk>/delete/", ColorDeleteAPIView.as_view(), name="color-delete"),
    
    # Size CRUD endpoints
    path("sizes/", SizeListAPIView.as_view(), name="size-list"),
    path("sizes/<int:pk>/", SizeRetrieveAPIView.as_view(), name="size-retrieve"),
    path("sizes/create/", SizeCreateAPIView.as_view(), name="size-create"),
    path("sizes/<int:pk>/update/", SizeUpdateAPIView.as_view(), name="size-update"),
    path("sizes/<int:pk>/delete/", SizeDeleteAPIView.as_view(), name="size-delete"),
    
    # Category CRUD endpoints
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("categories/<int:pk>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),
    
    # ProductVariant CRUD endpoints
    path("variants/", ProductVariantListAPIView.as_view(), name="product-variant-list"),
    path("variants/<int:pk>/", ProductVariantRetrieveAPIView.as_view(), name="product-variant-retrieve"),
    path("variants/create/", ProductVariantCreateAPIView.as_view(), name="product-variant-create"),
    path("variants/<int:pk>/update/", ProductVariantUpdateAPIView.as_view(), name="product-variant-update"),
    path("variants/<int:pk>/delete/", ProductVariantDeleteAPIView.as_view(), name="product-variant-delete"),
]
