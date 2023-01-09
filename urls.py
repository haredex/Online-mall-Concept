from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shoplist/', views.shoplist, name='shoplist'),
    path('shop/<str:shop_name>/', views.shop_detail, name='shop_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]