# Generated by Django 4.1.3 on 2022-12-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_donate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Availability'),
        ),
    ]
