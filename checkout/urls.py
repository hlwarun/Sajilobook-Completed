from django.urls import path
from checkout import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]
