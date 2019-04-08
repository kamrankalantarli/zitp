from django.db import models
from django.urls import reverse

class Kurs(models.Model):
    title = models.CharField(max_length=30,verbose_name="kurs adi")
    content = models.TextField(blank=True,verbose_name="haqqinda")
    image = models.ImageField(null=True,blank=True )
    height_field = models.IntegerField(default=0)
    publish=models.DateTimeField(auto_now=True,verbose_name="tarix")

    def get_absolute_url(self):
        return reverse('kurs:detail', kwargs={'id': self.id})


    class Meta:
        ordering= ['-publish' , 'id']