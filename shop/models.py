from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class AvailableProductManager(models.Manager):
    def get_querySet(self):
        return super(AvailableProductManager, self).get_queryset().filter(available=True)
     

class Product(models.Model):

    GENDER_CHOICES = (
        ('مردانه', 'مردانه'),
        ('زنانه', 'زنانه')
    )

    SEASON_CHOICES = (
        ('بهار', 'بهار'),
        ('تابستان', 'تابستان'),
        ('پاییز', 'پاییز'),
        ('زمستان', 'زمستان')
    )

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    size = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    season = models.CharField(max_length=50, choices=SEASON_CHOICES)
    #supplier = models.CharField(max_length=200)

    objects = models.Manager()  # The default manager
    available = AvailableProductManager()  # Our custom manager

    #quantity = models.IntegerField()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    # @property
    # def calculate_qty(self):
    #     return qty

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


# class Clothes(product):

#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )

#     SEASON_CHOICES = (
#         ('Sp', 'Spring'),
#         ('Su', 'Summer'),
#         ('Au', 'Autumn'),
#         ('W', 'Winter')
#     )

#     size = models.IntegerField()
#     gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
#     color = models.CharField(max_length=50)
#     material = models.CharField()
#     season = models.CharField(max_length=50, choices=SEASON_CHOICES)
#     supplier = models.CharField(max_length=200)

#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("shop:product_detail", args=[self.id, self.slug])