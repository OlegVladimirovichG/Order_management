from django.urls import path
from orders import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.create_order, name='create_order'),
    path('update/<int:pk>/', views.update_order, name='update_order'),
    path('cancel/<int:pk>/', views.cancel_order, name='cancel_order'),
    path('change_status/<int:pk>/', views.change_status, name='change_status'),
    path('delete/<int:pk>/', views.delete_order, name='delete_order'),
]