from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccesTemplateView)

app_name = 'orders'

urlpatterns = [

    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-success/', SuccesTemplateView.as_view(), name='order-success'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order-canceled'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('', OrderListView.as_view(), name='orders_list'),
]
