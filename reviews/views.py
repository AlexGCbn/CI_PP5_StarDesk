from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages


class AddReview(View):
    """Add review class based view"""

    def post(self, request, *args, **kwargs):
        """Handle POST to add new review"""
        if kwargs['category'] == 'case':
            product = Case.objects.get(id=kwargs['id'])
            form = CaseReviewForm(request.POST)
        elif kwargs['category'] == 'motherboard':
            product = Motherboard.objects.get(id=kwargs['id'])
            form = MotherboardReviewForm(request.POST)
        elif kwargs['category'] == 'cpu':
            product = Cpu.objects.get(id=kwargs['id'])
            form = CpuReviewForm(request.POST)
        elif kwargs['category'] == 'gpu':
            product = Gpu.objects.get(id=kwargs['id'])
            form = GpuReviewForm(request.POST)
        elif kwargs['category'] == 'ram':
            product = Ram.objects.get(id=kwargs['id'])
            form = RamReviewForm(request.POST)
        elif kwargs['category'] == 'psu':
            product = Psu.objects.get(id=kwargs['id'])
            form = PsuReviewForm(request.POST)
        elif kwargs['category'] == 'storage':
            product = Storage.objects.get(id=kwargs['id'])
            form = StorageReviewForm(request.POST)
        if form.is_valid():
            form.product = product
            form.save()
            messages.success(request, 'Review added successfully!')
        else: 
            messages.error(request, 'There was an error. Please try again.')

        return redirect(reverse('product_details', args={'category': product.category, 'id': product.id}))
