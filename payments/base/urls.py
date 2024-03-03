from django.urls import path

from .views import get_checkout_session, get_item_page, get_order_page, get_order_session, home

urlpatterns = [
    path('', home, name='home'),

    path('buy/<int:id>/', get_checkout_session, name='get_checkout_session'),
    path('item/<int:id>/', get_item_page, name='get_item_page'),

    path('order/<int:order_id>/', get_order_page, name='get_order_page'),
    path('order/<int:order_id>/checkout/', get_order_session, name='get_order_session'),
]
