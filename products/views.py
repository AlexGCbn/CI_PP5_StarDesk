from django.shortcuts import render
from django.views import generic, View
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class AllProductsView(View):
    """ View to display all products """

    def get(self, request):
        """ A view to return index page """
        # values info from here https://books.agiliq.com/projects/django-orm-cookbook/en/latest/union.html
        query_case = Case.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        query_mobo = Motherboard.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        query_cpu = Cpu.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        # query_cpu = Cpu.objects.all()
        query_gpu = Gpu.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        query_ram = Ram.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        query_psu = Psu.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        query_storage = Storage.objects.all().only(
            'model', 'manufacturer', 'price', 'rating', 'image'
        )
        products = query_case.union(
            query_mobo,
            # query_cpu,
            query_gpu,
            query_ram,
            query_psu,
            query_storage
        )
        template = 'products/products.html'
        context = {
            'products': products,
            'cpus': query_cpu
        }
        return render(request, template, context)
