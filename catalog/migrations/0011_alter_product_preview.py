# Generated by Django 4.2.3 on 2023-09-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, default='products/no_image.jpg', null=True, upload_to='products/', verbose_name='изображение'),
        ),
    ]
