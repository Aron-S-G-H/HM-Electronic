# Generated by Django 4.2.5 on 2023-11-12 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0013_remove_comment_email_remove_comment_user_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentreply',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'Comments Replies'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='response',
        ),
    ]
