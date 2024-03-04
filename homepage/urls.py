from django.urls import path
from .import views

urlpatterns =[
    
    path('',views.home,name='home'),
    path('dog/',views.dog,name='dog'),
     path('cart/',views.cart,name='cart')
]
