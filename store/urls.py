from django.urls import path
from . import views 


app_name = 'store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>', views.ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', views.remove_from_cart, name='remove-from-cart'),
    path('checkout/', views.checkout, name='checkout'),
]
