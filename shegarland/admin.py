from django.contrib import admin
from .models import ShegarLandForm
from .forms import ShegarLandFormForm

class ShegarLandFormAdmin(admin.ModelAdmin):
    form = ShegarLandFormForm  # Use the custom form

    list_display = (
        'Kutaamagaalaa',
        'Aanaa',
        'iddo_adda',
        'lakk_adda',
        'gosa_tajajila',
        'madda_lafa',
        'tajajila_iddo',
        'qamaa_qophaef',
        'tajajila_qophaef',
        'balina_lafa',
        'kan_qophesse',
        'shapefile',
        'Ragaa_biroo',
        'Mallattoo',
        'bal_lafa_bahi_tae',
        'bal_lafa_hafe',
        'qaama_bahi_tahef',
        'tajajila_bahi_tahef',
        'kan_bahi_taasise',
        'ragaittin_bahi_tae',
        'guyyaa_bahi_tae',
    )

    search_fields = (
        'Kutaamagaalaa', 'Aanaa','lakk_adda', 'iddo_adda', 'qamaa_qophaef','qaama_bahi_tahef','guyya_qophae', 'guyya_galmae',  
        'madda_lafa','kan_bahi_taasise','qamaa_qophaef','qaama_bahi_tahef','guyyaa_bahi_tae','tajajila_bahi_tahef',
    )
    list_filter = (
        'Kutaamagaalaa',
        'Aanaa',
         'balina_lafa',
        'gosa_tajajila',
        'madda_lafa',
        'haala_beenya',
        'tajajila_qophaef',
        'tajajila_iddo',
         'gosa_tajajila',
    )

    fields = [
        'Kutaamagaalaa', 'Aanaa', 'iddo_adda', 'lakk_adda', 
        'gosa_tajajila', 'madda_lafa', 'tajajila_iddo', 
        'haala_beenya', 'qamaa_qophaef', 'tajajila_qophaef', 
        'balina_lafa', 'kan_qophesse', 'guyya_qophae', 'guyya_galmae',  
        'shapefile', 'Ragaa_biroo', 'Mallattoo',  
        'bal_lafa_bahi_tae', 'bal_lafa_hafe', 
        'qaama_bahi_tahef', 'tajajila_bahi_tahef',
        'kan_bahi_taasise', 'guyyaa_bahi_tae', 'ragaittin_bahi_tae'
    ]

    def save_model(self, request, obj, form, change):
        # Check if 'suura_iddoo' field has a file
        if not obj.Ragaa_biroo:
            obj.Ragaa_biroo = None  # Handle missing Ragaa_biroo file

        # Check if 'ragaittin_bahi_tae' field has a file
        if not obj.ragaittin_bahi_tae:
            obj.ragaittin_bahi_tae = None  # Handle missing ragaittin_bahi_tae file

        super().save_model(request, obj, form, change)

# Register the model
admin.site.register(ShegarLandForm, ShegarLandFormAdmin)


from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')