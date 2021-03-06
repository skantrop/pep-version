from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['food']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    # list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    search_fields = ['id', 'first_name', 'last_name', 'email']
    list_per_page = 10


admin.site.register(Order, OrderAdmin)