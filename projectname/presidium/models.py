from django.db import models
from imagefield.fields import ImageField

# Create your models here.
class Presidium(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=100)
    image = ImageField(
        _('image'),
        upload_to='images/%Y/%m',
        blank=True,
        auto_add_fields=True,
    )

    def __str__(self):
        return self.name