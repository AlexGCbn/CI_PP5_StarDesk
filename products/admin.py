from django.contrib import admin
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage

admin.site.register(Case)
admin.site.register(Motherboard)
admin.site.register(Cpu)
admin.site.register(Gpu)
admin.site.register(Ram)
admin.site.register(Psu)
admin.site.register(Storage)
