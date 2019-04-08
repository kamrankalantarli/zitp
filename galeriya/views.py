from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from galeriya.models import Galeriya
from django.core.paginator import Paginator
from django.db.models import Q
def index(request):
    galeriya_list = Galeriya.objects.all()
    context = {
        'galeriya_list':galeriya_list,
    }

    return render(request,'galeriya/index.html',context)
def detail(request,id):
    gost = get_object_or_404(Galeriya,id=id)

    context={
        'gost': gost,

    }
    return render(request,'galeriya/index.html',context)