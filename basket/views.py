from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_basket(request):
    """A View that renders the basket contents page"""
    return render(request, "basket/basket.html")

@login_required
def add_to_basket(request, id):
    """Add a quantity of the specified service to the basket"""
    # quantity = int(request.POST.get('quantity'))
    quantity = 1
    basket = request.session.get('basket', {})
    basket[id] = basket.get(id, quantity)
    request.session['basket'] = basket
    return redirect(reverse('services'))

@login_required
def adjust_basket(request, id):
    """
    Adjust the quantity of the specified service to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
