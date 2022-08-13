from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    feedback,
    home,
    about,
    CartView,
    contact,
    add_to_cart,
    products,
    product_category,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    PostSearch,
    todays_deal
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('todays_deal/', todays_deal, name='todays_deal'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
    path('products/search', PostSearch, name='search-result'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/category/<str:slug>', product_category, name='product_category'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
