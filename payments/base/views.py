from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view

from django.conf import settings
import stripe
from rest_framework.response import Response

from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    context = {'items': items, 'orders': orders}
    return render(request, 'base/home.html', context)


@api_view(['GET'])
def get_checkout_session(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(item.get_absolute_url()),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
    )

    return Response({'session_id': session.id})


@api_view(['GET'])
def get_item_page(request, id):
    item = get_object_or_404(Item, id=id)
    serializer = ItemSerializer(item)

    return render(request, 'base/item.html', {'item': serializer.data})


@api_view(['GET'])
def get_order_page(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'base/order.html', {'order': order})


@api_view(['GET'])
def get_order_session(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Order {order.id}',
                    },
                    'unit_amount': int(order.calculate_total() * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(order.get_absolute_url()),
        cancel_url=request.build_absolute_uri(order.get_absolute_url()),
    )

    return Response({'session_id': session.id})
