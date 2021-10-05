# Generated by Django 3.2.7 on 2021-10-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
