from django.urls import path
from cart import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/<product_code>/', views.update_cart, name='update_cart'),
]
