# Generated by Django 4.2.5 on 2023-11-21 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_alter_sendemail_options_remove_contactus_situation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='file',
            field=models.FileField(blank=True, help_text='فایل های pdf و png و jpg مجاز هستند', null=True, upload_to='messages_file', verbose_name='فایل'),
        ),
        migrations.AlterField(
            model_name='sendemail',
            name='submit_status',
            field=models.BooleanField(default=False, verbose_name='وضعیت ارسال پیام'),
        ),
    ]