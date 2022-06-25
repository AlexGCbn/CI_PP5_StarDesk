from django import forms
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


class DealCaseForm(forms.ModelForm):

    class Meta:
        model = DealCase
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealMotherboardForm(forms.ModelForm):

    class Meta:
        model = DealMotherboard
        fields = ('product', 'price_new', 'deal_ends')

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealCpuForm(forms.ModelForm):

    class Meta:
        model = DealCpu
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealGpuForm(forms.ModelForm):

    class Meta:
        model = DealGpu
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealRamForm(forms.ModelForm):

    class Meta:
        model = DealRam
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealPsuForm(forms.ModelForm):

    class Meta:
        model = DealPsu
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealStorageForm(forms.ModelForm):

    class Meta:
        model = DealStorage
        fields = ('product', 'price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
