from django.urls import path
from . import views
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('', sign_up_by_django, name='sign_up_by_django'),
    path('up/', sign_up_by_html, name='sign_up_by_html'),
]