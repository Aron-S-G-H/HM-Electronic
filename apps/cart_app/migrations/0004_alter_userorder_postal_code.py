# Generated by Django 4.2.5 on 2023-10-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_remove_productorder_discount_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='postal_code',
            field=models.CharField(max_length=12, verbose_name='کد پستی'),
        ),
    ]