from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.ProductsDetailView.as_view(), name='detail'),
    path('checkout/',views.checkout, name='checkout'),
    path('register', views.register, name= 'register'),
    path('items/', views.items, name='items'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

