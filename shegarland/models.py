from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser,User
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.contrib.gis.db import models as gis_models

User = get_user_model()

# Custom Validator to ensure no digits before the decimal point
def validate_no_digits_before_decimal(value):
    """Ensure that there are no digits before the decimal point (only decimals allowed)."""
    if value and len(str(value).split('.')[0]) > 0:
        raise ValidationError("Ensure that there are no digits before the decimal point.")
    return value

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"Password reset request for {self.user.email}"


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True, null=True)

    def _str_(self):
        return self.email

    class Meta:
        permissions = (('can_view_user', 'Can view user'),)
        unique_together = (('email',),)
        ordering = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class ShegarLandForm(models.Model):
    # Choices for various fields
    Kutaamagaalaa_choices = [
        ('Sulultaa', 'Sulultaa'), ('M/Abbichuu', 'M/Abbichuu'), ('L/Xafoo L/Dadhii', 'L/Xafoo L/Dadhii'),
        ('K/Jiddaa', 'K/Jiddaa'), ('K/faccee', 'K/faccee'), ('Galaan', 'Galaan'),
        ('Furii', 'Furii'), ('G/Guddaa', 'G/Guddaa'), ('Sabbataa', 'Sabbataa'),
        ('M/Nonnoo', 'M/Nonnoo'), ('G/Gujee', 'G/Gujee'), ('Burrayyuu', 'Burrayyuu')
    ]

    madda_lafa_choices = [
        ('ISA Digame', 'ISA Digame'), 
        ('Waligalten kan cite', 'Waligalten kan cite'),
        ('Lafa motumma', 'Lafa motumma'),
        ('Lafa walini', 'Lafa walini'),
        ('Lafa benyan itti kaffalame', 'Lafa benyan itti kaffalame'),
        ('Lafa seran ala qabame bankitti debi\'e', 'Lafa seran ala qabame bankitti debi\'e'),
        ('kan biroo', 'kan biroo')
    ]

    haala_beenya_choices = [
        ('Bilisaa', 'Bilisaa'), 
        ('Beenyaa kan qabu', 'Beenyaa kan qabu')
    ]

    gosa_tajajila_choices = [
        ('Mana Jireenyaa', 'Mana Jireenyaa'), ('Daldala', 'Daldala'),
        ('Tajajilaa Bulchiinsaa', 'Tajajilaa Bulchiinsaa'), ('Tajajilaa Haw.', 'Tajajilaa Haw.'),
        ('Industirii/Investimenti/', 'Industirii/Investimenti/'), ('Iddoo Bashannanaa', 'Iddoo Bashannanaa'),
        ('Magarisumma', 'Magarisumma'), ('Lafa Bosona', 'Lafa Bosona'),
        ('Duwwaa/Open-Space/', 'Duwwaa/Open-Space/'), ('Qonnaa', 'Qonnaa'),
        ('Dhedicha', 'Dhedicha'), ('Iddo ISAn Digame', 'Iddo ISAn Digame'),
        ('Lafa Albudaa/Quarry Site/', 'Lafa Albudaa/Quarry Site/'), ('Kan biroo', 'Kan biroo')
    ]

    tajajila_qophaef_choices = [
        ('Bankii Lafa', 'Bankii Lafa'), ('Mana jirenya', 'Mana jirenya'),
        ('Daldala', 'Daldala'), ('Tajajilaa Bulchi', 'Tajajilaa Bulchi'),
        ('Tajajilaa Haw.', 'Tajajilaa Haw.'), ('Investimenti', 'Investimenti'),
        ('IMX', 'IMX'), ('Magarisumma', 'Magarisumma'),
        ('Innishetivif', 'Innishetivif'), ('Tajajila babalifanna', 'Tajajila babalifanna'),
        ('Qonnaa', 'Qonnaa'), ('Tajajila yeroof', 'Tajajila yeroof'),
        ('Tajaajila Babal', 'Tajaajila Babal')
    ]

    Aanaa_choices = [
        ('Abbaa Gadaa', 'Abbaa Gadaa'), ('wasarbii', 'wasarbii'),
        ('Tufaa munaa', 'Tufaa munaa'), ('A/M/Abbichuu', 'A/M/Abbichuu'),
        ('Eekkaa Daallee', 'Eekkaa Daallee'), ('Lagaa Dambal', 'Lagaa Dambal'),
        ('Ekkaa Sadeen', 'Ekkaa Sadeen'), ('Haroo Qullit', 'Haroo Qullit'),
        ('Dire_Sokkoruu', 'Dire Sokorruu'), ('Kuraa Jidda', 'Kuraa Jidda'),
        ('Galaan Arabsaa', 'Galaan Arabsaa'), ('Waddeessa', 'Waddeessa'),
        ('Tulluu Dimtuu', 'Tulluu Dimtuu'), ('Siidaa awaash', 'Siidaa awaash'),
        ('Galaan', 'Galaan'), ('Andoodee', 'Andoodee'), ('Mudaa Furii', 'Mudaa Furii'),
        ('Caffe karaabuu', 'Caffe karaabuu'), ('Gadaa Faajjii', 'Gadaa Faajjii'),
        ('Galaan Guddaa', 'Galaan Guddaa'), ('Lakkulee gejjaa', 'Lakkulee gejjaa'),
        ('Daalattii', 'Daalattii'), ('Meettaa', 'Meettaa'),
        ('Mogolee', 'Mogolee'), ('Caffee', 'Caffee'), ('M/gafarsaa', 'M/gafarsaa'),
        ('Nonnoo', 'Nonnoo'), ('Beeroo', 'Beeroo'), ('B/Kattaa', 'B/Kattaa'),
        ('L/kattaa', 'L/kattaa'), ('A/diimaa', 'A/diimaa'), ('G/burrayyuu', 'G/burrayyuu'),
        ('Egduu ilalaa', 'Egduu ilalaa'), ('Gujee', 'Gujee'), ('Koloboo', 'Koloboo')
    ]

    tajajila_iddo_choices = [
        ('Adminstration/AD/', 'Adminstration/AD/'), ('Commercial/CO/', 'Commercial/CO/'),
        ('Eco_Tourism/RE-5/', 'Eco_Tourism/RE-5/'), ('Formal Green', 'Formal Green'),
        ('Recreational & Environmental/RE/', 'Recreational & Environmental/RE/'), 
        ('Open Spaces and Sport Centers', 'Open Spaces and Sport Centers'),
        ('Pure Residence/R/', 'Pure Residence/R/'),
        ('Mixid Residence/R-2/', 'Mixid Residence/R-2/'), 
        ('Manufacturing and Storage/P-1/', 'Manufacturing and Storage/P-1/'),
        ('Social Service/S/', 'Social Service/S/'), 
        ('Special Function', 'Special Function'),
        ('Special residence', 'Special residence'), 
        ('Transport', 'Transport'),
        ('Urban Agriculture/UA/', 'Urban Agriculture'), 
        ('Logestic and Free Trade Zone', 'Logestic and Free Trade Zone'),
        ('River and Arteficial Lake', 'River and Arteficial Lake'),
        ('High Density Mixed Residence', 'High Density Mixed Residence')
    ]
    
    # Model fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Kutaamagaalaa = models.CharField(max_length=50, choices=Kutaamagaalaa_choices)
    Aanaa = models.CharField(max_length=50, choices=Aanaa_choices)
    iddo_adda = models.CharField(max_length=30, blank=True, null=True)
    lakk_adda = models.IntegerField(default=0, blank=True, null=True)
    gosa_tajajila = models.CharField(max_length=50, choices=gosa_tajajila_choices, blank=True, null=True)
    madda_lafa = models.CharField(max_length=50, choices=madda_lafa_choices)
    tajajila_iddo = models.CharField(max_length=60, choices=tajajila_iddo_choices)
    haala_beenya = models.CharField(max_length=20, choices=haala_beenya_choices)
    qamaa_qophaef = models.CharField(max_length=50, blank=True, null=True)
    tajajila_qophaef = models.CharField(max_length=50, choices=tajajila_qophaef_choices)
    balina_lafa = models.DecimalField(max_digits=10, decimal_places=2)
    lakk_xalayaa_murtoo = models.CharField(max_length=255, blank=True, null=True)
    sadarka_iddo = models.CharField(max_length=255, blank=True, null=True)
    gosa_investimentii = models.CharField(max_length=255, blank=True, null=True)
    sababa_qophaef = models.CharField(max_length=255, blank=True, null=True)
    kan_qophesse = models.CharField(max_length=40, default='user', blank=True, null=True)
    guyya_qophae = models.DateField()
    guyya_galmae = models.DateField(null=True, blank=True, default=datetime.date.today)

    ragaittin_bahi_tae = models.ImageField(upload_to='images/', blank=True, null=True)
    guyyaa_bahi_tae = models.DateField(blank=True, null=True)
    bal_lafa_bahi_tae = models.DecimalField(max_digits=8, decimal_places=6, default=0.0, blank=True, null=True)
    bal_lafa_hafe = models.DecimalField(max_digits=8, decimal_places=6, default=0.0, blank=True, null=True)

    qaama_bahi_tahef = models.CharField(max_length=40, blank=True, null=True)
    tajajila_bahi_tahef = models.CharField(max_length=40, blank=True, null=True)
    kan_bahi_taasise = models.CharField(max_length=255, blank=True, null=True)

    geom = gis_models.PolygonField(srid=32637, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.balina_lafa and not self.bal_lafa_hafe:
            self.bal_lafa_hafe = self.balina_lafa
        if self.balina_lafa and self.bal_lafa_bahi_tae:
            self.bal_lafa_hafe = self.balina_lafa - self.bal_lafa_bahi_tae
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Kutaamagaalaa}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def _str_(self):
        return f"Notification for {self.user.username}: {self.message}"
    
import datetime
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User

class Parcel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Kutaamagaalaa = models.CharField("Kutaa Magaalaa", max_length=50)
    Aanaa = models.CharField("Aanaa", max_length=50)
    iddo_adda = models.CharField("Iddoo Addaa", max_length=30, blank=True, null=True)
    lakk_adda = models.IntegerField( default=0, blank=True, null=True)
    gosa_tajajila = models.CharField( max_length=50)
    madda_lafa = models.CharField(max_length=50)
    tajajila_iddo = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
    land_use = models.CharField(max_length=100)
    haala_beenya = models.CharField(max_length=20)
    qamaa_qophaef = models.CharField(max_length=50)
    tajajila_qophaef = models.CharField(max_length=50)
    balina_lafa = models.DecimalField(max_digits=10, decimal_places=2)
    kan_qophesse = models.CharField(max_length=40, default='user', blank=True, null=True)
    guyya_qophae = models.DateField("Guyyaa Qophaaye")
    guyya_galmae = models.DateField("Guyyaa Galmaa'e", null=True, blank=True, default=datetime.date.today)
    geom = gis_models.PolygonField(srid=32637)

    def __str__(self):
        return f"{self.Kutaamagaalaa} "