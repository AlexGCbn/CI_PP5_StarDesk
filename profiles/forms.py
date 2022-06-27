from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        """
        Override init method to set placeholders,
        classes and set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'profile_full_name': 'Full Name',
            'profile_phone_number': 'Phone Number',
            'profile_postcode': 'Postal Code',
            'profile_city': 'City',
            'profile_street_address1': 'Street Address 1',
            'profile_street_address2': 'Street Address 2',
        }

        self.fields['profile_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'profile_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
