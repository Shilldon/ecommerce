from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

class OrderLineAdminInline(admin.TabularInline): # TabularInline subclass defines the template used to render the order in the admin interface. Stackedinline is another option
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, ) # admin interface has the ability to edit more that one model on a single page this is known as inlines

admin.site.register(Order, OrderAdmin)