from django.urls import path
from orders import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.create_order, name='create_order'),
    path('update/<int:pk>/', views.update_order, name='update_order'),
]