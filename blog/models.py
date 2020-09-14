from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase, TaggedItemBase
from django.contrib.contenttypes.models import ContentType

class CustomTag(TagBase):
    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"


class MyCustomTag(GenericTaggedItemBase, TaggedItemBase):

    tag = models.ForeignKey(
        CustomTag,
        on_delete=models.CASCADE,
        related_name="items",
    )

 
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='منتشر شده')

class Post(models.Model):
    STATUS_CHOICES = (
        ('در انتظار', 'در انتظار'),
        ('منتشر شده', 'منتشر شده'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='در انتظار')
    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager
    tags = TaggableManager(through=MyCustomTag)
    image = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg', blank=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

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
    body = models.TextField(max_length=1500)
    parent = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE)
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
        return Comments.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True