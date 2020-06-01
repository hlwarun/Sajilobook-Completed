from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('academic/', views.academic, name='academic'),
    path('non_academic/', views.non_academic, name='non_academic'),
    path('contact/', views.contact, name='contact'),
    path('sell/', views.sell, name='sell'),
    path('<product_code>/', views.single, name='single'),
]
