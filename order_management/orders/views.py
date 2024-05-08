from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from django.urls import reverse
from .models import Order
from .forms import DeleteOrderForm
from django.contrib import messages


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            customer_name = form.cleaned_data['customer_name']
            status = form.cleaned_data['status']

            # Создаем новый заказ, учитывая введенный статус
            Order.objects.create(customer_name=customer_name, status=status)

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


def change_status(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:  # Проверяем, есть ли значение статуса
            order.status = new_status  # Устанавливаем новый статус заказа
            order.save()  # Сохраняем изменения
            return HttpResponseRedirect(reverse('order_list'))  # Перенаправляем на список заказов
        else:
            # Если значение статуса не передано, отобразите сообщение об ошибке или выполните другие действия
            # Например:
            messages.error(request, 'Status value is missing.')
            return HttpResponseRedirect(reverse('change_status', args=(pk,)))
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
        form = DeleteOrderForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == 'pass':
                order.delete()
                messages.success(request, 'Order deleted successfully.')
                return redirect('order_list')
            else:
                messages.error(request, 'Incorrect password. Please try again.')
    else:
        form = DeleteOrderForm()
    return render(request, 'orders/delete_order.html', {'form': form})
