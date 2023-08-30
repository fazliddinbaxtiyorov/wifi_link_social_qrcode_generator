from django.urls import path
from . import views

urlpatterns = [
    path('wifi/', views.wifi_qr_code, name='wifi'),
    path('link/', views.link_qr_code, name='link'),
    path('twitter/', views.twitter, name='twitter'),
    path('telegram/', views.telegram, name='telegram'),
    path('instagram/', views.instagram, name='instagram'),
]