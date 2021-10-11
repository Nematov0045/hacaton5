from django.urls import path
from .views import homepage,cart,cart2,contact,addToCart
urlpatterns=[
    path('', homepage,name='homepage'),
    path('cart', cart,name='cart'),
    path('cart2', cart2,name='cart2'),
    path('contact', contact,name='contact'),
    path('addToCart/<int:pk>', addToCart, name='addToCart'),
]