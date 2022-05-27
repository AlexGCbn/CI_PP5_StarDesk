from django.shortcuts import render
from django.views import View
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class AllProductsView(View):
    """ View to display all products """

    def get(self, request):
        """ A view to return index page """
        # values info from here https://books.agiliq.com/projects/django-orm-cookbook/en/latest/union.html
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
        template = 'products/products.html'
        context = {
            'products': products
        }
        return render(request, template, context)


class ProductDetails(View):
    """ Displays product details """

    def get(self, request, id, category):
        """ GET request for product details page """
        if category == 'case':
            product = Case.objects.get(id=id)
        elif category == 'motherboard':
            product = Motherboard.objects.get(id=id)
        elif category == 'cpu':
            product = Cpu.objects.get(id=id)
        elif category == 'gpu':
            product = Gpu.objects.get(id=id)
        elif category == 'ram':
            product = Ram.objects.get(id=id)
        elif category == 'psu':
            product = Psu.objects.get(id=id)
        elif category == 'storage':
            product = Storage.objects.get(id=id)

        template = 'products/product_details.html'
        context = {
            'product': product
        }
        return render(request, template, context)
