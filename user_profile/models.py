from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
#from django.core.validators import RegexValidator



class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('مرد', 'مرد'),
        ('زن', 'زن'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    #phone_number_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    postal_code = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    home_telephone = PhoneNumberField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg', blank=True)

    def __str__(self):
        return f"Profile for user {self.user.username}"

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

