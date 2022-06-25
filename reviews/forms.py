from django import forms
from .models import CaseReview, MotherboardReview, CpuReview, GpuReview, RamReview, PsuReview, StorageReview


class CaseReviewForm(forms.ModelForm):

    class Meta:
        model = CaseReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MotherboardReviewForm(forms.ModelForm):

    class Meta:
        model = MotherboardReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CpuReviewForm(forms.ModelForm):

    class Meta:
        model = CpuReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GpuReviewForm(forms.ModelForm):

    class Meta:
        model = GpuReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RamReviewForm(forms.ModelForm):

    class Meta:
        model = RamReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PsuReviewForm(forms.ModelForm):

    class Meta:
        model = PsuReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StorageReviewForm(forms.ModelForm):

    class Meta:
        model = StorageReview
        except = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
