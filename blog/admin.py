from django.contrib import admin
from blog.models import Blog,Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','user','publish']
    list_display_links = ['title','user']
    class Meta:
        model = Blog
admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','user','create_data']
    list_display_links = ['blog','user','create_data']
    class Meta:
        model = Comment
admin.site.register(Comment,CommentAdmin)

# Register your models here.
