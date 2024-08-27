from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DeleteOrderForm

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
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def change_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
            return redirect('order_list')
        else:
            messages.error(request, 'Status value is missing.')
            return redirect('change_status', pk=pk)
    else:
        return render(request, 'orders/change_status.html', {'order': order})

def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = 'cancelled'
    order.save()
    return redirect('order_list')

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')  # Обновите с правильным именем вашего URL-namespace
    return redirect('orders:order_list')

