from django import forms
from .models import DealCase, DealMotherboard, DealCpu, DealGpu, DealRam, DealPsu, DealStorage


class DealCaseForm(forms.ModelForm):

    class Meta:
        model = DealCase
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealMotherboardForm(forms.ModelForm):

    class Meta:
        model = DealMotherboard
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealCpuForm(forms.ModelForm):

    class Meta:
        model = DealCpu
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealGpuForm(forms.ModelForm):

    class Meta:
        model = DealGpu
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealRamForm(forms.ModelForm):

    class Meta:
        model = DealRam
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealPsuForm(forms.ModelForm):

    class Meta:
        model = DealPsu
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DealStorageForm(forms.ModelForm):

    class Meta:
        model = DealStorage
        exclude = ('price_was', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
