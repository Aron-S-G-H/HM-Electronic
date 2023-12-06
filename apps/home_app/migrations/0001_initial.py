# Generated by Django 4.2.1 on 2023-09-08 10:36

import apps.home_app.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='عنوان')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name='توضیحات')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='BannerSectionOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(help_text='اندازه تصاویر 450x450 پیکسل باشد', upload_to='banners', verbose_name='عکس بنر')),
                ('category_slug', models.SlugField(allow_unicode=True, help_text='اسلاگ دسته بندی را که مربوط به این تصویر است را وارد کنبد', verbose_name='اسلاگ دسته بندی تصویر')),
                ('category_id', models.SmallIntegerField(help_text='ID دسته بندی مربوط به این تصویر را وارد کنید', unique=True, verbose_name='ID دسته بندی تصویر ')),
                ('upload_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپلود')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')),
            ],
            options={
                'verbose_name': 'بنر بخش اول',
                'verbose_name_plural': 'بنرهای بخش اول',
                'ordering': ('-upload_at',),
            },
        ),
        migrations.CreateModel(
            name='BannerSectionTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(help_text='حداقل عرض 2000px و حداقل ارتفاع 800px', upload_to='banners', verbose_name='عکس بنر')),
                ('category_slug', models.SlugField(allow_unicode=True, help_text='اسلاگ دسته بندی را که مربوط به این تصویر است را وارد کنبد', verbose_name='اسلاگ دسته بندی تصویر')),
                ('category_id', models.SmallIntegerField(help_text='ID دسته بندی مربوط به این تصویر را وارد کنید', unique=True, verbose_name='ID دسته بندی تصویر ')),
                ('upload_at', models.DateField(auto_now_add=True, verbose_name='تاریخ آپلود')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')),
            ],
            options={
                'verbose_name': 'بنر بخش دوم',
                'verbose_name_plural': 'بنرهای بخش دوم',
                'ordering': ('-upload_at',),
            },
        ),
        migrations.CreateModel(
            name='CommunicationWays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, help_text='۱۰۰ کاراکتر مجاز است - optional', max_length=100, null=True, verbose_name='آدرس')),
                ('email', models.EmailField(blank=True, help_text='optional', max_length=254, null=True, verbose_name='ایمیل')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')),
            ],
            options={
                'verbose_name': 'راه ارتباطی',
                'verbose_name_plural': 'راه های ارتباطی',
            },
        ),
        migrations.CreateModel(
            name='FQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='۱۵۰ کاراکتر مجاز است', max_length=150, unique=True, verbose_name='عنوان سوال')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='پاسخ')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت انتشار در وبسایت')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به آپدیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'سوال متداول',
                'verbose_name_plural': 'سوالات متداول',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='تصویر لوگو')),
                ('status', models.BooleanField(default=True, help_text='در صورت غیرفعال کردن در وبسایت نمایش داده نمی شود', verbose_name='وضعیت نمایش در سایت')),
                ('upload_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپلود')),
            ],
            options={
                'verbose_name': 'لوگو',
                'verbose_name_plural': 'لوگو',
            },
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='۴۰ کاراکتر مجاز است', max_length=40, unique=True, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')),
            ],
            options={
                'verbose_name': 'روش ارسال',
                'verbose_name_plural': 'روش های ارسال',
            },
        ),
        migrations.CreateModel(
            name='SliderBannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(help_text='حداقل ارتفاع تصویر 675px باشد', upload_to='home_slider', verbose_name='عکس بنر')),
                ('title', models.CharField(blank=True, help_text='۳۰ کاراکتر مجاز است - optional', max_length=30, null=True, verbose_name='سر تیتر')),
                ('sub_title', models.CharField(blank=True, help_text='۴۰ کاراکتر مجاز است - optional', max_length=40, null=True, verbose_name='تیتر')),
                ('description', models.CharField(blank=True, help_text='۴۰ کاراکتر مجاز است - optional', max_length=40, null=True, verbose_name='متن')),
                ('status', models.BooleanField(default=True, help_text='در صورت غیرفعال کردن در وبسایت نمایش داده نمی شود', verbose_name='وضعیت نمایش در سایت')),
                ('upload_at', models.DateField(auto_now_add=True, verbose_name='تاریخ آپلود')),
            ],
            options={
                'verbose_name': 'بنر اسلایدر',
                'verbose_name_plural': 'بنرهای اسلایدر',
            },
        ),
        migrations.CreateModel(
            name='SliderLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(help_text='حداقل اندازه تصویر 390x75px یاشد', upload_to='logo_slider', verbose_name='تصویر لوگو')),
                ('status', models.BooleanField(default=True, help_text='در صورت غیرفعال کردن در وبسایت نمایش داده نمی شود', verbose_name='وضعیت نمایش در سایت')),
                ('upload_at', models.DateField(auto_now_add=True, verbose_name='تاریخ آپلود')),
            ],
            options={
                'verbose_name': 'لوگو شرکت',
                'verbose_name_plural': 'لوگو شرکت ها',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('instagram', 'اینستاگرام'), ('facebook', 'فیسبوک'), ('linkedin', 'لینکدین'), ('twitter', 'توییتر'), ('telegram', 'تلگرام')], max_length=50, verbose_name='عنوان')),
                ('icon', models.ImageField(help_text='ایکون مدنظر را در فرمت svg با png و بدون پس زمینه در حداقل سابز 50x50 آپلود کنید ', null=True, upload_to='social-icon', verbose_name='ایکون')),
                ('link', models.URLField(verbose_name='لینک')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('communication_ways', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='home_app.communicationways', verbose_name='راه ارتباطی')),
            ],
            options={
                'verbose_name': 'شبکه مجازی',
                'verbose_name_plural': 'شبکه های مجازی',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='مثال: بخش فنی و تعمیرات', max_length=30, verbose_name='عنوان بخش')),
                ('phone_number', models.PositiveIntegerField(help_text='مثال:۹۱۲۲۳۴۵۶۸۹', validators=[apps.home_app.models.phone_number_validator], verbose_name='شماره همراه')),
                ('communication_ways', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_n', to='home_app.communicationways', verbose_name='راه ارتباطی')),
            ],
            options={
                'verbose_name': 'شماره همراه',
                'verbose_name_plural': 'شمارهای همراه',
            },
        ),
        migrations.CreateModel(
            name='CompanyNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_code', models.CharField(help_text='مثال: ۰۲۱', max_length=3, verbose_name='کد استان')),
                ('number', models.PositiveIntegerField(blank=True, help_text='مثال: ۶۶۶۷۸۹۰۸', null=True, validators=[apps.home_app.models.company_number_validator], verbose_name='شماره ثابت')),
                ('communication_ways', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_n', to='home_app.communicationways', verbose_name='راه ارتباطی')),
            ],
            options={
                'verbose_name': 'شماره ثابت',
                'verbose_name_plural': 'شماره های ثابت',
            },
        ),
        migrations.CreateModel(
            name='AboutUsFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='۲۵ کاراکتر', max_length=25, unique=True, verbose_name='عنوان')),
                ('description', models.CharField(help_text='۳۰ کاراکتر', max_length=30, verbose_name='توضیح')),
                ('icon', models.ImageField(help_text='ایکون مدنظر را در فرمت svg یا png و بدون پس زمینه در حداقل سابز 50x50 آپلود کنید ', upload_to='aboutUs_icon', verbose_name='ایکون')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('about_us', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='home_app.aboutus', verbose_name='درباره ما')),
            ],
            options={
                'verbose_name': 'ویژگی',
                'verbose_name_plural': 'ویژگی ها',
            },
        ),
    ]
