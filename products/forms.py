from django import forms
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        exclude = ('rating', )


class MotherboardForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        exclude = ('rating', )


class CpuForm(forms.ModelForm):

    class Meta:
        model = Cpu
        exclude = ('rating', )


class GpuForm(forms.ModelForm):

    class Meta:
        model = Gpu
        exclude = ('rating', )


class RamForm(forms.ModelForm):

    class Meta:
        model = Ram
        exclude = ('rating', )


class PsuForm(forms.ModelForm):

    class Meta:
        model = Psu
        exclude = ('rating', )


class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        exclude = ('rating', )
