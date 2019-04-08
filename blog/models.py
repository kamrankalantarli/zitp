from django.db import models
from django.urls import reverse


class Blog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=80,verbose_name="Başlıq")
    content = models.TextField(blank=True,verbose_name="Xəbər")
    publish = models.DateTimeField(auto_now= True, verbose_name="Tarix")
    image = models.ImageField(null=True,blank=True )

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})


    class Meta:
        ordering= ['-publish' , 'id']

class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog = models.ForeignKey('blog.Blog' ,related_name='comments', on_delete=models.CASCADE )
    content = models.TextField(verbose_name="şərh")
    create_data = models.DateTimeField(auto_now=True)

