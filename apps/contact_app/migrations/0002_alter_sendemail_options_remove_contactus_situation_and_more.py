# Generated by Django 4.2.5 on 2023-11-20 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendemail',
            options={'verbose_name': 'ارسال ایمیل به کاربر', 'verbose_name_plural': 'ارسال ایمیل به کاربران'},
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='situation',
        ),
        migrations.RemoveField(
            model_name='sendemail',
            name='contact_us',
        ),
        migrations.RemoveField(
            model_name='sendemail',
            name='submit',
        ),
        migrations.AddField(
            model_name='sendemail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL, verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='sendemail',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='موضوع'),
        ),
    ]
