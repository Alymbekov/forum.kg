from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', related_name='children', blank=True, null=True,on_delete=models.CASCADE
        )
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

