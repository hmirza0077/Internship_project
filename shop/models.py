from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from django.conf import settings
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableQuerySet

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, unique=True, db_index=True),
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class AvailableProductManager(models.Manager):
    def get_querySet(self):
        return super(AvailableProductManager, self).get_queryset().filter(available=True)
     

class Product(TranslatableModel):

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

    COLOR_CHOICES = (
        ('red', 'قرمز'),
        ('brown', 'قهوه ای'),
        ('yellow', 'زرد'),
        ('black', 'مشکی'),
        ('blue', 'آبی'),
        ('green', 'سبز'),
        ('pink', 'صورتی'),
        ('gray', 'خاکستری'),
    )

    # SIZE_CHOICES = (
    #     ('XS', 'XS'),
    #     ('S', 'S'),
    #     ('M', 'M'),
    #     ('L', 'L'),
    #     ('XL', 'XL'),
    #     ('XXL', 'XXL'),
    # )

    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        short_description = RichTextUploadingField('توضیحات مختصر', blank=True, null=True),
        long_description = RichTextUploadingField('توضیحات جامع', blank=True, null=True),
        material = models.CharField(max_length=50),
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # description = models.TextField(blank=True)
    visit_num = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    size = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    color = MultiSelectField(choices=COLOR_CHOICES)
    #color = models.CharField(max_length=50)
    season = models.CharField(max_length=50, choices=SEASON_CHOICES)
    #supplier = models.ForeignKet(Supplier, related_name='suppliers', on_delete=models.CASCADE)

    # objects = models.Manager()  # The default manager
    # available = AvailableProductManager()  # Our custom manager

    #quantity = models.IntegerField()

    class Meta:
        # ordering = ('name',)
        # index_together = (('id', 'slug'),)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    # @property
    # def calculate_qty(self):
    #     return qty

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


class CommentManager(models.Manager):
    def all_comments(self):
        qs = super().filter(parent=None)
        return qs

class ProductComments(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=1500)
    parent = models.ForeignKey('ProductComments', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-created']
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return str(self.user.username)

    def children(self): # replies
        return ProductComments.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


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