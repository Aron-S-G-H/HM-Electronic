# Generated by Django 4.2.5 on 2023-10-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_alter_communicationways_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderbannerimage',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='sliderbannerimage',
            name='category_slug',
        ),
        migrations.AddField(
            model_name='sliderbannerimage',
            name='url_address',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس URL'),
        ),
    ]