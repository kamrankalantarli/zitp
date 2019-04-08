from django.db import models
from django.urls import reverse

# Create your models here.
class Galeriya(models.Model):
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('galeriya', kwargs={'id': self.id})
