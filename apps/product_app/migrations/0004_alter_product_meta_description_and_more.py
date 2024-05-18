# Generated by Django 4.2.5 on 2024-01-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_alter_category_icon_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(help_text='150 کاراکتر', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='img',
            field=models.ImageField(help_text='اندازه تصویر : 800 × 800', upload_to='product', verbose_name='عکس محصول'),
        ),
    ]
