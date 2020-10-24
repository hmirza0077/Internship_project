from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class ActiveCouponManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCouponManager, self).get_queryset().filter(active=True)

class Coupon(models.Model):
    #user = models.ManyToManyField("User", verbose_name=_(""))
    code = models.CharField(_('کد'), max_length=50, unique=True)
    valid_from = models.DateTimeField(_('اعتبار از'))
    valid_to = models.DateTimeField(_('اعتبار تا'))
    discount = models.IntegerField(_('تخفیف'),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active = models.BooleanField()

    objects = models.Manager()
    is_active = ActiveCouponManager()

    class Meta:
        ordering = ('-valid_from',)
        verbose_name = _("کوپن")
        verbose_name_plural = _("کوپن ها")

    def __str__(self):
        return self.code
