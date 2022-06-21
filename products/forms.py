from django import forms
from .models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MotherboardForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CpuForm(forms.ModelForm):

    class Meta:
        model = Cpu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GpuForm(forms.ModelForm):

    class Meta:
        model = Gpu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RamForm(forms.ModelForm):

    class Meta:
        model = Ram
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PsuForm(forms.ModelForm):

    class Meta:
        model = Psu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
