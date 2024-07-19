# Generated by Django 5.0.7 on 2024-07-18 09:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
