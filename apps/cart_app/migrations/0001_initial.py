# Generated by Django 4.2.5 on 2023-12-14 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره همراه')),
                ('state', models.CharField(max_length=40, verbose_name='استان')),
                ('city', models.CharField(max_length=40, verbose_name='شهر')),
                ('postal_code', models.CharField(max_length=12, verbose_name='کد پستی')),
                ('national_code', models.CharField(max_length=20, verbose_name='کد ملی')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('note', models.TextField(blank=True, null=True, verbose_name='یادداشت کاربر')),
                ('total_price', models.PositiveIntegerField(verbose_name='هزینه کل')),
                ('is_paid', models.BooleanField(default=False, verbose_name='وضعیت پرداخت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت سفارش')),
                ('reference_id', models.CharField(blank=True, max_length=15, null=True, verbose_name='کد پیگیری سفارش')),
                ('is_sms_sent', models.BooleanField(blank=True, default=False, null=True, verbose_name='اس ام اس ارسال شده')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_uniqueID', models.CharField(max_length=110, verbose_name='product unique id')),
                ('product_price', models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='تعداد')),
                ('item_total', models.PositiveIntegerField(verbose_name='مجموع قیمت')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='cart_app.userorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product_app.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'سفارش محصول',
                'verbose_name_plural': 'سفارش محصولات',
            },
        ),
    ]
