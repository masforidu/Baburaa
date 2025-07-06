from django import forms
from .models import ShegarLandForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ShegarLandFormForm(forms.ModelForm):
    guyya_qophae = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    guyyaa_bahi_tae = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    guyya_galmae = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)  # ✅ Fixed from _init to _init_

        if user and not user.is_staff:
            read_only_fields = [
                'bal_lafa_bahi_tae', 'bal_lafa_hafe', 'qaama_bahi_tahef',
                'tajajila_bahi_tahef', 'kan_bahi_taasise', 'guyyaa_bahi_tae',
            ]
            for field in read_only_fields:
                if field in self.fields:
                    self.fields[field].widget.attrs['readonly'] = True
                    self.fields[field].label += " (Admin only)"

    class Meta:
        model = ShegarLandForm
        fields = [
            'Kutaamagaalaa', 'Aanaa', 'iddo_adda', 'lakk_adda', 'gosa_tajajila',
            'madda_lafa', 'tajajila_iddo', 'haala_beenya', 'qamaa_qophaef',
            'tajajila_qophaef', 'balina_lafa', 'lakk_xalayaa_murtoo', 'sadarka_iddo',
            'gosa_investimentii', 'sababa_qophaef', 'kan_qophesse', 'guyya_qophae',
            'bal_lafa_bahi_tae', 'bal_lafa_hafe', 'qaama_bahi_tahef',
            'tajajila_bahi_tahef', 'kan_bahi_taasise', 'ragaittin_bahi_tae',
            'guyyaa_bahi_tae', 'guyya_galmae'
        ]
        exclude = ['user', 'geom']

    def clean_lakk_adda(self):
        lakk_adda = self.cleaned_data.get('lakk_adda')
        if lakk_adda is not None and lakk_adda < 0:
            raise forms.ValidationError("Lakk adda must be a positive integer.")
        return lakk_adda

from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        exclude = ['owner', 'geom']
        widgets = {
            'guyya_qophae': forms.DateInput(attrs={'type': 'date'}),
            'guyya_galmae': forms.DateInput(attrs={'type': 'date'}),
        }