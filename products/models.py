from django.db import models

MOBO_SIZES = (
    ('mini_atx', 'Mini ATX'),
    ('micro_atx', 'Micro ATX'),
    ('atx', 'ATX'),
    ('e_atx', 'EATX')
)

RATING = (
    (1, 'Very Dissatisfied'),
    (2, 'Dissatisfied'),
    (3, 'Neutral'),
    (4, 'Satisfied'),
    (5, 'Very Satisfied')
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


class Case(models.Model):
    """ Case products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    mobo_sizes = models.CharField(choices=MOBO_SIZES, max_length=254)

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Motherboard(models.Model):
    """ Motherboard products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    size = models.CharField(choices=MOBO_SIZES, max_length=254)
    socket = models.CharField(choices=CPU_SOCKETS, max_length=254)
    ram_type = models.CharField(choices=RAM_TYPES, max_length=254)

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Cpu(models.Model):
    """ CPU products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    socket = models.CharField(choices=CPU_SOCKETS, max_length=254)
    core_count = models.IntegerField()

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Gpu(models.Model):
    """ GPU products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    speed = models.IntegerField()
    memory_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Psu(models.Model):
    """ PSU products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    wattage = models.IntegerField()
    category = models.CharField(choices=PSU_CATEGORIES, max_length=254)

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Storage(models.Model):
    """ Storage products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    capacity = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'


class Ram(models.Model):
    """ RAM products model """
    model = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, choices=RATING)
    speed = models.IntegerField()
    capacity = models.IntegerField()
    type = models.CharField(choices=RAM_TYPES, max_length=254)

    def __str__(self):
        return f'{self.model} by {self.manufacturer}'
