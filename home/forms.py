from django import forms
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


class DealCaseForm(forms.ModelForm):

    class Meta:
        model = DealCase
        fields = ('price_new', 'deal_ends')

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
        fields = ('price_new', 'deal_ends')

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealCpuForm(forms.ModelForm):

    class Meta:
        model = DealCpu
        fields = ('price_new', 'deal_ends')

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
        fields = ('price_new', 'deal_ends')

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
        fields = ('price_new', 'deal_ends')

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
        fields = ('price_new', 'deal_ends')

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
        fields = ('price_new', 'deal_ends')

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
