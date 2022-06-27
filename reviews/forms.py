from django import forms
from .models import (
    CaseReview, MotherboardReview,
    CpuReview, GpuReview,
    RamReview, PsuReview,
    StorageReview
)


class CaseReviewForm(forms.ModelForm):

    class Meta:
        model = CaseReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MotherboardReviewForm(forms.ModelForm):

    class Meta:
        model = MotherboardReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CpuReviewForm(forms.ModelForm):

    class Meta:
        model = CpuReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GpuReviewForm(forms.ModelForm):

    class Meta:
        model = GpuReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RamReviewForm(forms.ModelForm):

    class Meta:
        model = RamReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PsuReviewForm(forms.ModelForm):

    class Meta:
        model = PsuReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StorageReviewForm(forms.ModelForm):

    class Meta:
        model = StorageReview
        exclude = ('product', 'user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
