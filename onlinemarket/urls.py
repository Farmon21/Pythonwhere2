from django.urls import path
from .views import (products_list,
                    cart,
                    delete_cart_item,
                    edit_cart_item,
                    product_detail,
                    create_order,
                    rate_product,
                    orders
                    )

urlpatterns = [
    path('', products_list, name='product_list'),
    path('cart/', cart, name='cart'),
    path('item/<int:pk>/delete/', delete_cart_item, name='delete_item'),
    path('edit_cart_item<int:pk>/', edit_cart_item, name='edit_cart_item'),
    path('product/<int:pk>/detail/', product_detail, name='product_detail'),
    path('cart/create_order/item/', create_order, name='create_order'),
    path('rate_product/<int:pk>/', rate_product, name='rate_product'),
    path('orders/', orders, name='orders'),
]
