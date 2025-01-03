# Generated by Django 5.1.1 on 2024-12-23 21:21

import shegarland.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shegarland', '0009_alter_shegarlandform_aanaa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shegarlandform',
            name='bal_lafa_bahi_tae',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=8, null=True, validators=[shegarland.models.validate_no_digits_before_decimal]),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='bal_lafa_hafe',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=8, null=True, validators=[shegarland.models.validate_no_digits_before_decimal]),
        ),
    ]
