# Generated by Django 4.2.5 on 2023-10-13 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_alter_product_best_seller_alter_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='best_seller',
        ),
    ]