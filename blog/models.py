from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager
# from taggit.models import TagBase, GenericTaggedItemBase, TaggedItemBase
# from django.contrib.contenttypes.models import ContentType
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField
# from parler.managers import TranslatableQuerySet, TranslatableManager
from django.utils.translation import gettext_lazy as _

# class CustomTag(TagBase):
#     class Meta:
#         verbose_name = "برچسب"
#         verbose_name_plural = "برچسب ها"


# class MyCustomTag(GenericTaggedItemBase, TaggedItemBase):

#     tag = models.ForeignKey(
#         CustomTag,
#         on_delete=models.CASCADE,
#         related_name="items",
#     )

class Tags(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('عنوان'), unique=True, max_length=50, db_index=True),
        slug = models.SlugField(unique=True, max_length=50, db_index=True)
    )

    class Meta:
        verbose_name = _("برچسب")
        verbose_name_plural = _("برچسب ها")

    def __str__(self):
        return self.name

 
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('عنوان'), max_length=50, db_index=True),
        slug = models.SlugField(max_length=50, db_index=True)
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status='منتشر شده')

class Post(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(_('عنوان'), max_length=250),
        # slug = models.SlugField(max_length=250, unique_for_date='publish'),
        slug = models.SlugField(max_length=250),
        short_description = RichTextUploadingField(_('توضیحات مختصر'), blank=True, null=True),
        long_description = RichTextUploadingField(_('توضیحات جامع'), blank=True, null=True),
    )

    STATUS_CHOICES = (
        ('waiting', _('در انتظار')),
        ('published', _('منتشر شده')),
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    publish = models.DateTimeField(_('تاریخ انتشار'), default=timezone.now)
    created = models.DateTimeField(_('تاریخ ساخت'), auto_now_add=True)
    updated = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)
    status = models.CharField(_('وضعیت'), max_length=10, choices=STATUS_CHOICES, default='waiting')
    # objects = models.Manager()  # The default manager
    # published = PublishedManager()  # Our custom manager
    tags = models.ManyToManyField('Tags',related_name='posts', blank=True)
    image = models.ImageField(_('تصویر'), upload_to='users/%Y/%m/%d', default='default.jpg', blank=True)

    class Meta:
        #ordering = ('-publish',)
        verbose_name = _("پست")
        verbose_name_plural = _("پست ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail",
                        args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class CommentManager(models.Manager):
    def all_comments(self):
        qs = super().filter(parent=None)
        return qs

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(_('متن پیام'), max_length=1500)
    parent = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(_('تاریخ ساخت'), auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-created']
        verbose_name = _("کامنت")
        verbose_name_plural = _("کامنت ها")

    def __str__(self):
        return str(self.user.username)

    def children(self): # replies
        return Comments.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True