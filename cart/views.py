from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Food
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    food = get_object_or_404(Food, id=product_id)
    if request.method == "POST":
        form = CartAddProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("cleaned_data here", form.cleaned_data)
            # product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            # update_quantity = form.cleaned_data['update_quantity']
            cart.add(product=food, quantity=quantity)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Food, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'detail.html', {'cart': cart})