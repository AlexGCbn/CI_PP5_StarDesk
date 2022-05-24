from django.contrib import admin
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'mobo_sizes')
    list_display = ('model', 'manufacturer', 'price', 'mobo_sizes')
    search_fields = ['model', 'manufacturer']


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'size', 'socket', 'ram_type')
    list_display = ('model', 'manufacturer', 'price', 'size', 'socket', 'ram_type')
    search_fields = ['model', 'manufacturer']


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'socket', 'core_count')
    list_display = ('model', 'manufacturer', 'price', 'socket', 'core_count')
    search_fields = ['model', 'manufacturer']


@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'speed', 'memory_capacity')
    list_display = ('model', 'manufacturer', 'price', 'speed', 'memory_capacity')
    search_fields = ['model', 'manufacturer']


@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'speed', 'capacity', 'type')
    list_display = ('model', 'manufacturer', 'price', 'speed', 'capacity', 'type')
    search_fields = ['model', 'manufacturer']


@admin.register(Psu)
class PsuAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'wattage', 'category')
    list_display = ('model', 'manufacturer', 'price', 'wattage', 'category')
    search_fields = ['model', 'manufacturer']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_filter = ('model', 'manufacturer', 'price', 'speed', 'capacity')
    list_display = ('model', 'manufacturer', 'price', 'speed', 'capacity')
    search_fields = ['model', 'manufacturer']
