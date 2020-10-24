from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    
    # DELIVERY_CHOICES = (
    #     ('Free', 'رایگان'),
    #     ('Pishtaz', 'پیشتاز'),
    #     ('Sefareshi', 'سفارشی')
    # )

    first_name = models.CharField(_('نام کوچک'), max_length=50)
    last_name = models.CharField(_('نام خانوادگی'), max_length=50)
    email = models.EmailField(_('ایمیل'))
    address = models.CharField(_('آدرس'), max_length=250)
    postal_code = models.CharField(_('کد پستی'), max_length=20)
    city = models.CharField(_('شهر'), max_length=100)
    created = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    updated = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)
    paid = models.BooleanField(_('وضعیت پرداخت'), default=False)
    # Coupons
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(_('تخفیف'), default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = _('سفارش')
        verbose_name_plural = _('سفارشات')

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))
class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(_('قیمت'), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('تعداد'), default=1)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity
