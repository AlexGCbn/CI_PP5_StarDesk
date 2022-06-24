from django import forms
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


class DealCaseForm(forms.ModelForm):

    class Meta:
        model = DealCase
        readonly_fields = ('product', )
        exclude = ('price_was', )

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
        readonly_fields = ('product', )
        exclude = ('price_was', )

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealCpuForm(forms.ModelForm):

    class Meta:
        model = DealCpu
        readonly_fields = ('product', )
        exclude = ('price_was', )

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
        readonly_fields = ('product', )
        exclude = ('price_was', )

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
        readonly_fields = ('product', )
        exclude = ('price_was', )

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
        readonly_fields = ('product', )
        exclude = ('price_was', )

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
        readonly_fields = ('product', )
        exclude = ('price_was', )

        field_classes = {
            'deal_ends': forms.DateTimeField,
        }

        widgets = {
            'deal_ends': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
