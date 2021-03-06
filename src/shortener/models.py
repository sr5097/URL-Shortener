from django.db import models
from django.utils.translation import activate
from .utils import code_generator, create_shortcode

# Create your models here.

class ShortenerURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortenerURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = ShortenerURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class ShortenerURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #shortcode = models.CharField(max_length=15, null=False, blank=False)

    objects = ShortenerURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode== "":
            self.shortcode = create_shortcode(self)
        super(ShortenerURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)