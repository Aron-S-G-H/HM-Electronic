# Generated by Django 4.2.5 on 2023-11-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, help_text='اندازه تصویر 1024x683px باشد', null=True, upload_to='blog_image', verbose_name='تصویر'),
        ),
    ]