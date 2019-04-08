from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from blog.models import Blog
from blog.forms import BlogForm, CommentForm
from django.db.models import Q
def index(request):
    post = Blog.objects.all()


    query = request.GET.get('q')
    if query:
        post = post.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)

        ).distinct()




    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        lost = form.save(commit=False)
        lost.user = request.user
        lost.save()

        return HttpResponseRedirect(lost.get_absolute_url())

    context = {
        'form': form,
        'post':post,
    }

    return render(request,'blog/index.html',context)

def detail(request,id):
    lost = get_object_or_404(Blog,id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.blog = lost
        comment.save()
        return HttpResponseRedirect(lost.get_absolute_url())
    context={
        'form': form,
        'lost': lost,

    }
    return render(request,'blog/detail.html',context)
