from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ActiveCouponManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCouponManager, self).get_queryset().filter(active=True)

class Coupon(models.Model):
    #user = models.ManyToManyField("User", verbose_name=_(""))
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active = models.BooleanField()

    objects = models.Manager()
    is_active = ActiveCouponManager()

    class Meta:
        ordering = ('-valid_from',)
        verbose_name = "کوپن"
        verbose_name_plural = "کوپن ها"

    def __str__(self):
        return self.code
