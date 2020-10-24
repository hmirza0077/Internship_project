from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class ContactUsMessage(models.Model):
    name = models.CharField(_('نام فرستنده'), max_length=200, help_text="Name of the sender")
    email = models.EmailField(_('ایمیل'), max_length=200)
    phone_number = PhoneNumberField(_('شماره تلفن'), null=True, blank=True)
    subject = models.CharField(_('موضوع پیام'), null=True, blank=True, max_length=200)
    body = models.TextField(_('متن پیام'))
    created_date = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)

    class Meta:
        verbose_name = _('تماس با ما')
        verbose_name_plural = _('تماس با ما')

    def __str__(self):
        return f"{self.name} - {self.email}"