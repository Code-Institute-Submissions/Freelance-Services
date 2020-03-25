from django.shortcuts import get_object_or_404
from services.models import Service


def basket_contents(request):
    """
    Used to store basket data across all pages, 
    This means that the user can browse the site without losing the basket contents..
    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    service_count = 0
    for id, quantity in basket.items():
        service = get_object_or_404(Service, pk=id)
        total += quantity * service.price
        service_count += quantity
        basket_items.append({'id': id, 'quantity': quantity, 'service': service})

    return {'basket_items':basket_items, 'total': total, 'service_count': service_count}
