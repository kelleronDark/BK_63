# Generated by Django 4.2.4 on 2023-09-23 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advert', '0002_rename_decription_advert_description'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advert',
            table='advertisements',
        ),
    ]