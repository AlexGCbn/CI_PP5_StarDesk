from django.contrib import admin
from .models import CaseReview, MotherboardReview, CpuReview, GpuReview, RamReview, PsuReview, StorageReview


@admin.register(CaseReview)
class CaseReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(MotherboardReview)
class MotherboardReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(CpuReview)
class CpuReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(GpuReview)
class GpuReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(RamReview)
class RamReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(PsuReview)
class PsuReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]


@admin.register(StorageReview)
class StorageReviewAdmin(admin.ModelAdmin):
    list_filter = ('product', 'user')
    list_display = ('product', 'user', 'score')
    search_fields = ['product', 'user',]
