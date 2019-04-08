from django.db import models
from django.urls import reverse


class Eventa(models.Model):
    title = models.CharField(max_length=80,verbose_name="Başlıq")
    content = models.TextField(blank=True,verbose_name="Xəbər")
    publish = models.DateTimeField(auto_now= False, verbose_name="Tarix")
    image = models.ImageField(null=True,blank=True )

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'id': self.id})


    class Meta:
        ordering= ['-publish' , 'id']