# Generated by Django 4.2.4 on 2023-09-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('decription', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('auction', models.BooleanField(help_text='Отметьте, уместен ли торг', verbose_name='Торг')),
            ],
        ),
    ]
