from django.contrib import admin
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


@admin.register(DealCase)
class CaseDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealMotherboard)
class MotherboardDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealCpu)
class CpuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealGpu)
class GpuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealRam)
class RamDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealPsu)
class PsuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )


@admin.register(DealStorage)
class StorageDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'price_was', 'deal_ends')
    search_fields = ['product']
    readonly_fields = ('price_was', )