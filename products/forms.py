from django import forms
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MotherboardForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CpuForm(forms.ModelForm):

    class Meta:
        model = Cpu
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GpuForm(forms.ModelForm):

    class Meta:
        model = Gpu
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RamForm(forms.ModelForm):

    class Meta:
        model = Ram
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PsuForm(forms.ModelForm):

    class Meta:
        model = Psu
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        exclude = ('rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
