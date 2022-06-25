from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.views import View
from reviews.forms import (
    CaseReviewForm, MotherboardReviewForm,
    CpuReviewForm, GpuReviewForm,
    RamReviewForm, PsuReviewForm,
    StorageReviewForm
)
from home.models import (
    DealCase, DealMotherboard,
    DealCpu, DealGpu, DealRam,
    DealPsu, DealStorage
)
from .forms import (
    CaseForm, MotherboardForm,
    CpuForm, GpuForm,
    RamForm, PsuForm,
    StorageForm
)
from .models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)


class AllProductsView(View):
    """ View to display all products """

    def get(self, request):
        """ A view to return index page """

        # Category listing
        category = None
        if 'category' in request.GET:
            category = request.GET['category']

        # Search query
        query = None
        queries = None
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))
            queries = (
                Q(model__icontains=query) |
                Q(manufacturer__icontains=query) |
                Q(description__icontains=query)
            )

        # If category exists, query by it
        if category:
            if category == 'case':
                products = Case.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'motherboard':
                products = Motherboard.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'cpu':
                products = Cpu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'gpu':
                products = Gpu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'ram':
                products = Ram.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'psu':
                products = Psu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            elif category == 'storage':
                products = Storage.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
        else:
            # If queries exist (search), query by it
            if queries:
                query_case = Case.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_mobo = Motherboard.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_cpu = Cpu.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_gpu = Gpu.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_ram = Ram.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_psu = Psu.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_storage = Storage.objects.filter(queries).only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            # Get all products
            else:
                query_case = Case.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_mobo = Motherboard.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_cpu = Cpu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_gpu = Gpu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_ram = Ram.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_psu = Psu.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
                query_storage = Storage.objects.all().only(
                    'id', 'model', 'manufacturer',
                    'price', 'rating', 'image', 'category'
                )
            products = query_case.union(
                query_mobo,
                query_cpu,
                query_gpu,
                query_ram,
                query_psu,
                query_storage
            )

        # Sorting
        sort = None
        direction = None
        current_sorting = "None_None"
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = sort
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort = f'-{sort}'
            products = products.order_by(sort)
            current_sorting = f'{sortkey}_{direction}'

        template = 'products/products.html'
        context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            'category': category,
        }
        return render(request, template, context)


class ProductDetails(View):
    """ Displays product details """

    def get(self, request, id, category):
        """ GET request for product details page """
        if category == 'case':
            product = Case.objects.get(id=id)
            form = CaseReviewForm(request.POST)
            try:
                deal = DealCase.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'motherboard':
            product = Motherboard.objects.get(id=id)
            form = MotherboardReviewForm(request.POST)
            try:
                deal = DealMotherboard.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'cpu':
            product = Cpu.objects.get(id=id)
            form = CpuReviewForm(request.POST)
            try:
                deal = DealCpu.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'gpu':
            product = Gpu.objects.get(id=id)
            form = GpuReviewForm(request.POST)
            try:
                deal = DealGpu.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'ram':
            product = Ram.objects.get(id=id)
            form = RamReviewForm(request.POST)
            try:
                deal = DealRam.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'psu':
            product = Psu.objects.get(id=id)
            form = PsuReviewForm(request.POST)
            try:
                deal = DealPsu.objects.filter(product=product)[0]
            except IndexError:
                deal = []
        elif category == 'storage':
            product = Storage.objects.get(id=id)
            form = StorageReviewForm(request.POST)
            try:
                deal = DealStorage.objects.filter(product=product)[0]
            except IndexError:
                deal = []

        template = 'products/product_details.html'
        context = {
            'product': product,
            'form': form,
            'deal': deal,
        }
        return render(request, template, context)

    def post(self, request, id, category):
        """ POST request for adding items to Bag """

        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if quantity >= 1 and quantity <= 99:
            item = category + '_' + str(id)
            if item in list(bag.keys()):
                bag[item] += quantity
            else:
                bag[item] = quantity

        product_name = request.POST.get('product_friendly_name')
        request.session['bag'] = bag
        messages.success(request, f'Added {quantity}x {product_name} to your bag.')
        return redirect(redirect_url)


class AdminProductView(View):
    """
    Class Based View for adding products
    Only accessible by superusers
    """

    def get(self, request, *args, **kwargs):
        """
        GET request to display forms on page
        """
        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        template = 'products/add_product.html'
        case_form = CaseForm()
        motherboard_form = MotherboardForm()
        cpu_form = CpuForm()
        gpu_form = GpuForm()
        ram_form = RamForm()
        psu_form = PsuForm()
        storage_form = StorageForm()
        context = {
            'case_form': case_form,
            'motherboard_form': motherboard_form,
            'cpu_form': cpu_form,
            'gpu_form': gpu_form,
            'ram_form': ram_form,
            'psu_form': psu_form,
            'storage_form': storage_form,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        """
        POST request to handle form submission
        Reads the category and makes POST based on it
        """
        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        category = request.POST.get('category')
        if category == 'case':
            form = CaseForm(request.POST, request.FILES)
        elif category == 'motherboard':
            form = MotherboardForm(request.POST, request.FILES)
        elif category == 'cpu':
            form = CpuForm(request.POST, request.FILES)
        elif category == 'gpu':
            form = GpuForm(request.POST, request.FILES)
        elif category == 'ram':
            form = RamForm(request.POST, request.FILES)
        elif category == 'psu':
            form = PsuForm(request.POST, request.FILES)
        elif category == 'storage':
            form = StorageForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_details', id=new_product.id, category=category)
        else:
            messages.error(request, 'There was an error adding product.')
            return redirect('admin_add_product')


class ManageProduct(View):
    """
    Class based view for editing/deleting products
    """

    def get(self, request, *args, **kwargs):
        """
        GET request to display edit form
        """
        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        template = 'products/edit_product.html'
        if kwargs['category'] == 'case':
            product = Case.objects.get(id=kwargs['id'])
            form = CaseForm(instance=product)
        elif kwargs['category'] == 'motherboard':
            product = Motherboard.objects.get(id=kwargs['id'])
            form = MotherboardForm(instance=product)
        elif kwargs['category'] == 'cpu':
            product = Cpu.objects.get(id=kwargs['id'])
            form = CpuForm(instance=product)
        elif kwargs['category'] == 'gpu':
            product = Gpu.objects.get(id=kwargs['id'])
            form = GpuForm(instance=product)
        elif kwargs['category'] == 'ram':
            product = Ram.objects.get(id=kwargs['id'])
            form = RamForm(instance=product)
        elif kwargs['category'] == 'psu':
            product = Psu.objects.get(id=kwargs['id'])
            form = PsuForm(instance=product)
        elif kwargs['category'] == 'storage':
            product = Storage.objects.get(id=kwargs['id'])
            form = StorageForm(instance=product)
        context = {
            'form': form,
            'category': product.category,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        """
        POST request to edit/delete product
        """
        if not request.user.is_superuser:
            messages.error(request, 'Access denied!')
            return redirect(reverse('products'))

        if kwargs['category'] == 'case':
            product = Case.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'motherboard':
            product = Motherboard.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'cpu':
            product = Cpu.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'gpu':
            product = Gpu.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'ram':
            product = Ram.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'psu':
            product = Psu.objects.get(id=kwargs['id'])
        elif kwargs['category'] == 'storage':
            product = Storage.objects.get(id=kwargs['id'])
        if kwargs['operation'] == 'edit':
            if kwargs['category'] == 'case':
                form = CaseForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'motherboard':
                form = MotherboardForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'cpu':
                form = CpuForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'gpu':
                form = GpuForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'ram':
                form = RamForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'psu':
                form = PsuForm(request.POST, request.FILES, instance=product)
            elif kwargs['category'] == 'storage':
                form = StorageForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product edited successfully!')
                return redirect('product_details', id=kwargs['id'], category=kwargs['category'])
        elif kwargs['operation'] == 'delete':
            product.delete()
            return redirect('products')
