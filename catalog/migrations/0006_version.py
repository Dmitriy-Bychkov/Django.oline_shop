# Generated by Django 4.2.3 on 2023-08-22 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=100, verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=100, verbose_name='название версии')),
                ('is_current_version', models.BooleanField(default=False, verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
        ),
    ]