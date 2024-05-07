from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})


def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})


def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = 'cancelled'
    order.save()
    return redirect('order_list')
