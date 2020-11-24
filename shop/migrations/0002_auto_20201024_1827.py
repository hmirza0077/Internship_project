# Generated by Django 2.2.16 on 2020-10-24 14:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('red', 'قرمز'), ('brown', 'قهوه ای'), ('yellow', 'زرد'), ('black', 'مشکی'), ('blue', 'آبی'), ('green', 'سبز'), ('pink', 'صورتی'), ('gray', 'خاکستری')], max_length=43, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'مردانه'), ('women', 'زنانه')], max_length=50, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='در دسترس'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.CharField(choices=[('spring', 'بهار'), ('summer', 'تابستان'), ('autumn', 'پاییز'), ('winter', 'زمستان')], max_length=50, verbose_name='فصل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=15, verbose_name='سایز'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='visit_num',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='productcomments',
            name='body',
            field=models.TextField(max_length=1500, verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='productcomments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='material',
            field=models.CharField(max_length=50, verbose_name='نوع جنس'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='عنوان'),
        ),
    ]
