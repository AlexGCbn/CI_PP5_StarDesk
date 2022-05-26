from django.shortcuts import render
from django.views import generic, View
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class AllProductsView(View):
    """ View to display all products """

    def get(self, request):
        """ A view to return index page """
        # values_list info from here https://books.agiliq.com/projects/django-orm-cookbook/en/latest/union.html
        query_case = Case.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_mobo = Motherboard.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_cpu = Cpu.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_gpu = Gpu.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_ram = Ram.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_psu = Psu.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
        )
        query_storage = Storage.objects.all().values_list(
            'model', 'manufacturer', 'price', 'rating'
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
            'products': products,
        }
        return render(request, template, context)
