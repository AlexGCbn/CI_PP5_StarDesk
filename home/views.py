from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from products.models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)
from .models import (
    DealCase, DealMotherboard,
    DealCpu, DealGpu, DealRam,
    DealPsu, DealStorage
)
from .forms import (
    DealCaseForm, DealMotherboardForm,
    DealCpuForm, DealGpuForm, DealRamForm,
    DealPsuForm, DealStorageForm
)


class IndexView(View):
    """ Basic index view """

    def get(self, request):
        """ A view to return index page """
        template = 'home/index.html'
        return render(request, template)


class AdminAddDeal(View):
    """Class Based View for admins to add deals/offers"""

    def get(self, request, *args, **kwargs):
        """GET request to get add deal page"""

        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        template = 'home/add_deal.html'
        if kwargs['category'] == 'case':
            product = Case.objects.get(id=kwargs['id'])
            form = DealCaseForm(initial={'product': product})
        elif kwargs['category'] == 'motherboard':
            product = Motherboard.objects.get(id=kwargs['id'])
            form = DealMotherboardForm(initial={'product': product})
        elif kwargs['category'] == 'cpu':
            product = Cpu.objects.get(id=kwargs['id'])
            form = DealCpuForm(initial={'product': product})
        elif kwargs['category'] == 'gpu':
            product = Gpu.objects.get(id=kwargs['id'])
            form = DealGpuForm(initial={'product': product})
        elif kwargs['category'] == 'ram':
            product = Ram.objects.get(id=kwargs['id'])
            form = DealRamForm(initial={'product': product})
        elif kwargs['category'] == 'psu':
            product = Psu.objects.get(id=kwargs['id'])
            form = DealPsuForm(initial={'product': product})
        elif kwargs['category'] == 'storage':
            product = Storage.objects.get(id=kwargs['id'])
            form = DealStorageForm(initial={'product': product})
        context = {
            'product': product,
            'form': form,
            'category': product.category,
        }
        return render(request, template, context)
    
    def post(self, request, *args, **kwargs):
        """POST request handling to add new deal"""
        
        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        category = request.POST.get('category')
        if category == 'case':
            form = DealCaseForm(request.POST, request.FILES)
        elif category == 'motherboard':
            form = DealMotherboardForm(request.POST, request.FILES)
        elif category == 'cpu':
            form = DealCpuForm(request.POST, request.FILES)
        elif category == 'gpu':
            form = DealGpuForm(request.POST, request.FILES)
        elif category == 'ram':
            form = DealRamForm(request.POST, request.FILES)
        elif category == 'psu':
            form = DealPsuForm(request.POST, request.FILES)
        elif category == 'storage':
            form = DealStorageForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_deal = form.save()
            messages.success(request, 'Deal added successfully!')
            return redirect('product_details', id=new_deal.product.id, category=category)
        else:
            messages.error(request, 'There was an error adding product.')
            return redirect('admin_add_product')
