from django.db import models

MOBO_SIZES = (
    ('mini_atx', 'Mini ATX'),
    ('micro_atx', 'Micro ATX'),
    ('atx', 'ATX'),
    ('e_atx', 'EATX')
)

CPU_SOCKETS = (
    ('AM4', 'AM4'),
    ('1700', '1700'),
    ('1200', '1200'),
    ('2066', '2066')
)

RAM_TYPES = (
    ('ddr3', 'DDR3'),
    ('ddr4', 'DDR4'),
    ('ddr5', 'DDR5'),
)

PSU_CATEGORIES = (
    ('80plus', '80 PLUS'),
    ('80plus_bronze', '80 PLUS Bronze'),
    ('80plus_silver', '80 PLUS Silver'),
    ('80plus_gold', '80 PLUS Gold'),
    ('80plus_platinum', '80 PLUS Platinum'),
    ('80plus_titanium', '80 PLUS Titanium')
)


class Product(models.Model):
    """Main product class"""
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f'{self.manufacturer} - {self.model}'

    def update_ratings(self, total_ratings, total_score):
        """Update rating function"""
        if total_score > 0:
            self.rating = total_score / total_ratings
        else:
            self.rating = None
        self.save()

    class Meta:
        abstract = True


class Case(Product):
    """ Case products model """
    mobo_sizes = models.CharField(choices=MOBO_SIZES, max_length=254)
    category = models.CharField(
        default='case', max_length=20, editable=False
    )


class Motherboard(Product):
    """ Motherboard products submodel """
    size = models.CharField(choices=MOBO_SIZES, max_length=254)
    socket = models.CharField(choices=CPU_SOCKETS, max_length=254)
    ram_type = models.CharField(choices=RAM_TYPES, max_length=254)
    category = models.CharField(
        default='motherboard', max_length=20, editable=False
    )


class Cpu(Product):
    """ CPU products submodel """
    socket = models.CharField(choices=CPU_SOCKETS, max_length=254)
    core_count = models.IntegerField()
    category = models.CharField(
        default='cpu', max_length=20, editable=False
    )


class Gpu(Product):
    """ GPU products submodel """
    speed = models.IntegerField()
    memory_capacity = models.IntegerField()
    category = models.CharField(
        default='gpu', max_length=20, editable=False
    )


class Ram(Product):
    """ RAM products submodel """
    speed = models.IntegerField()
    capacity = models.IntegerField()
    type = models.CharField(choices=RAM_TYPES, max_length=254)
    category = models.CharField(
        default='ram', max_length=20, editable=False
    )


class Psu(Product):
    """ PSU products submodel """
    wattage = models.IntegerField()
    e_category = models.CharField(choices=PSU_CATEGORIES, max_length=254)
    category = models.CharField(
        default='psu', max_length=20, editable=False
    )


class Storage(Product):
    """ Storage products submodel """
    capacity = models.IntegerField()
    speed = models.IntegerField()
    category = models.CharField(
        default='storage', max_length=20, editable=False
    )
