from django.urls import path
from .views import cart_home, cart_update, items_count

urlpatterns = [
    path('', cart_home, name='cart'),
    path('update/', cart_update, name='update'),
    path('items_count/', items_count, name='items_count'),
]
