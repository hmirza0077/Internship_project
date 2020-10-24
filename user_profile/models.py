from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
#from django.core.validators import RegexValidator



class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('male', _('مرد')),
        ('femal', _('زن'))
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(_('شماره تلفن همراه'), null=True, blank=True)
    postal_code = models.IntegerField(_('کد پستی'), blank=True, null=True)
    address = models.CharField(_('آدرس'), max_length=250, null=True, blank=True)
    home_telephone = PhoneNumberField(_('شماره تلفن ثابت'), null=True, blank=True, unique=True)
    gender = models.CharField(_('جنسیت'), max_length=5, choices=GENDER_CHOICES)
    city = models.CharField(_('شهر'), max_length=100)
    photo = models.ImageField(_('عکس پروفایل'), upload_to='users/%Y/%m/%d', default='default.jpg', blank=True)

    def __str__(self):
        return f"Profile for user {self.user.username}"

    class Meta:
        verbose_name = _('پروفایل')
        verbose_name_plural = _('پروفایل ها')

