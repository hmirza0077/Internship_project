from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from django.conf import settings
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

class BookmarkProduct(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product', related_name="products", on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bookmark_product"
        # ordering = ('-created',)
        verbose_name = _('لیست علاقه مندی ها')
        verbose_name_plural = _('لیست علاقه مندی ها')

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('عنوان'), max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, unique=True, db_index=True),
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = _('دسته بندی محصولات')
        verbose_name_plural = _('دسته بندی محصولات')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])

# class ProductQuerySet(TranslatableQuerySet, TreeQuerySet):
#     def as_manager(cls):
#         manager = AvailableProductManager.from_queryset(cls)()
#         manager._built_with_as_manager = True
#         return manager
#     as_manager.queryset_only = True
#     as_manager = classmethod(as_manager)

# class AvailableProductManager(TreeManager, TranslatableManager):
#     _queryset_class = ProductQuerySet
#     def get_querySet(self):
#         return super(AvailableProductManager, self).get_queryset().filter(available=True)
     

class Product(TranslatableModel):

    GENDER_CHOICES = (
        ('men', _('مردانه')),
        ('women', _('زنانه'))
    )

    SEASON_CHOICES = (
        ('spring', _('بهار')),
        ('summer', _('تابستان')),
        ('autumn', _('پاییز')),
        ('winter', _('زمستان')),
    )

    COLOR_CHOICES = (
        ('red', _('قرمز')),
        ('brown', _('قهوه ای')),
        ('yellow', _('زرد')),
        ('black', _('مشکی')),
        ('blue', _('آبی')),
        ('green', _('سبز')),
        ('pink', _('صورتی')),
        ('gray', _('خاکستری')),
    )

    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )

    translations = TranslatedFields(
        name = models.CharField(_('عنوان'), max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        short_description = RichTextUploadingField(_('توضیحات مختصر'), blank=True, null=True),
        long_description = RichTextUploadingField(_('توضیحات جامع'), blank=True, null=True),
        material = models.CharField(_('نوع جنس'), max_length=50),
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(_('تصویر محصول'), upload_to='products/%Y/%m/%d', blank=True, null=True)
    visit_num = models.PositiveIntegerField(_('تعداد بازدید'), default=0)
    price = models.PositiveIntegerField(_('قیمت'), default=0)
    is_available = models.BooleanField(_('در دسترس'), default=True)
    created = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    updated = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)

    size = MultiSelectField(_('سایز'), choices=SIZE_CHOICES)
    gender = models.CharField(_('جنسیت'), max_length=50, choices=GENDER_CHOICES)
    color = MultiSelectField(_('رنگ'), choices=COLOR_CHOICES)
    season = models.CharField(_('فصل'), max_length=50, choices=SEASON_CHOICES)
    #supplier = models.ForeignKet(Supplier, related_name='suppliers', on_delete=models.CASCADE)

    # objects = models.Manager()  # The default manager
    # available = AvailableProductManager()  # Our custom manager

    #quantity = models.IntegerField()

    class Meta:
        # ordering = ('name',)
        # index_together = (('id', 'slug'),)
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')

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
    body = models.TextField(_('متن پیام'), max_length=1500)
    parent = models.ForeignKey('ProductComments', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-created']
        verbose_name = _("کامنت")
        verbose_name_plural = _("کامنت ها")

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