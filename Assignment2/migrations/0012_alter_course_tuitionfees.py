# Generated by Django 5.1.3 on 2024-12-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment2', '0011_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='TuitionFees',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
