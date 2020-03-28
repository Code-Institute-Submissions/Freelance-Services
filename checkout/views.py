from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.conf import settings 
from django.utils import timezone
from .models import OrderLineItem
from .forms import PaymentForm, OrderForm
from services.models import Service
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    """
    Used to process payment, 
    """
    if not request.session.get('basket', {}):
        return redirect(reverse('services'))
    else:      
        if request.method=='POST':
            order_form = OrderForm(request.POST) # gets order form from POST
            payment_form = PaymentForm(request.POST) # gets Payment form from POST

            if order_form.is_valid() and payment_form.is_valid(): # Checks if forms are valid
                order = order_form.save(commit=False) 
                order.date = timezone.now()
                order.save()


                basket = request.session.get('basket', {}) #gets basket contents
                total = 0 # sets total to 0 for later
                for id, quantity in basket.items(): # Loops through basket items
                    service = get_object_or_404(Service, pk=id)
                    total += quantity * service.price
                    order_line_item = OrderLineItem(
                        order = order, 
                        service = service, 
                        quantity = quantity
                    )
                    order_line_item.save()
                try: # trys to make strip payment
                    customer = stripe.Charge.create(
                        amount = int(total * 100),
                        currency = "GBP",
                        description = request.user.email,
                        card = payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError: # returns error if there is an issue
                    messages.error(request, 'Your card was declined!')

                if customer.paid: 
                    messages.error(request, 'Payment Successful')
                    request.session['basket'] = {} # clears basket
                    return redirect(reverse('services'))
                else:
                    messages.error(request, "Unable to take payment")
                    print('im here')
            else:
                print(payment_form.errors)
                messages.error(request, "We were unable to take a payment with that card")
        else:
            payment_form = PaymentForm()
            order_form = OrderForm()

    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})