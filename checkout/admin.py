from django.contrib import admin
from .models import Order, OrderLineCase, OrderLineCpu, OrderLineGpu, OrderLineMotherboard, OrderLinePsu, OrderLineRam, OrderLineStorage


class OrderLineCaseAdminInline(admin.TabularInline):
    model = OrderLineCase
    readonly_fields = ('lineitem_total',)


class OrderLineMoboAdminInline(admin.TabularInline):
    model = OrderLineMotherboard
    readonly_fields = ('lineitem_total',)


class OrderLineCpuAdminInline(admin.TabularInline):
    model = OrderLineCpu
    readonly_fields = ('lineitem_total',)


class OrderLineGpuAdminInline(admin.TabularInline):
    model = OrderLineGpu
    readonly_fields = ('lineitem_total',)


class OrderLineRamAdminInline(admin.TabularInline):
    model = OrderLineRam
    readonly_fields = ('lineitem_total',)


class OrderLinePsuAdminInline(admin.TabularInline):
    model = OrderLinePsu
    readonly_fields = ('lineitem_total',)


class OrderLineStorageAdminInline(admin.TabularInline):
    model = OrderLineStorage
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderLineCaseAdminInline,
        OrderLineMoboAdminInline,
        OrderLineCpuAdminInline,
        OrderLineGpuAdminInline,
        OrderLineRamAdminInline,
        OrderLinePsuAdminInline,
        OrderLineStorageAdminInline,
    )

    readonly_fields = (
        'order_number', 'date',
        'delivery_cost', 'order_total',
        'grand_total', 'original_bag',
        'stripe_pid',
    )

    fields = (
        'order_number', 'date', 'full_name',
        'email', 'phone_number', 'country',
        'postcode', 'city', 'street_address1',
        'street_address2', 'delivery_cost',
        'order_total', 'grand_total',
        'original_bag', 'stripe_pid',
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'order_total', 'delivery_cost',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
