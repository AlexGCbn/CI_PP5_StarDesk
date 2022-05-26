from django.shortcuts import render
from django.views import generic, View
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class AllProductsView(View):
    """ View to display all products """

    def get(self, request):
        """ A view to return index page """
        query_case = Case.objects.all()
        query_mobo = Motherboard.objects.all()
        query_cpu = Cpu.objects.all()
        query_gpu = Gpu.objects.all()
        query_ram = Ram.objects.all()
        query_psu = Psu.objects.all()
        query_storage = Storage.objects.all()
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
