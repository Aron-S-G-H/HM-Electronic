# Generated by Django 4.2.5 on 2024-01-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_alter_bannersectionone_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynumber',
            name='province_code',
            field=models.CharField(help_text='مثال: 021', max_length=3, verbose_name='کد استان'),
        ),
    ]
