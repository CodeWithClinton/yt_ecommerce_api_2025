# Generated by Django 5.1.6 on 2025-04-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0010_customeraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
