from django.contrib import admin
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


@admin.register(DealCase)
class CaseDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealMotherboard)
class MotherboardDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealCpu)
class CpuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealGpu)
class GpuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealRam)
class RamDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealPsu)
class PsuDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']


@admin.register(DealStorage)
class StorageDealAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    list_display = ('product', 'price_new', 'deal_ends')
    search_fields = ['product']