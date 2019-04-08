from django.shortcuts import render
from blog.models import Blog
from ipaddr import client_ip
from kurs.models import Kurs
from events.models import Eventa


def homel(request):
    media = Kurs.objects.all()
    tedbr=Eventa.objects.all()
    bloge=Blog.objects.all()


    ipaddr = client_ip(request)



    context={
        'bloge':bloge,
        'tedbr':tedbr,
        'media':media,
    }

    return render(request,'home/homes.html',context)

