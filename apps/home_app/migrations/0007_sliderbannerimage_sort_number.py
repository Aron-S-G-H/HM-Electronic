# Generated by Django 4.2.5 on 2023-10-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_remove_bannersectionone_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderbannerimage',
            name='sort_number',
            field=models.PositiveSmallIntegerField(null=True, unique=True, verbose_name='اولویت نمایش'),
        ),
    ]
