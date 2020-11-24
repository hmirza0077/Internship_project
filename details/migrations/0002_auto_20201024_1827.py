# Generated by Django 2.2.16 on 2020-10-24 14:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactusmessage',
            options={'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس با ما'},
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='body',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='name',
            field=models.CharField(help_text='Name of the sender', max_length=200, verbose_name='نام فرستنده'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='موضوع پیام'),
        ),
    ]