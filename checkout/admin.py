from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

#Used to register orders within the admin portal. 
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)

admin.site.register(Order, OrderAdmin)