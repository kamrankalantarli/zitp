from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from kurs.models import Kurs
from django.core.paginator import Paginator
from django.db.models import Q
def index(request):
    kurs_list = Kurs.objects.all()

    context = {
        'kurs_list':kurs_list,
    }

    return render(request,'kurs/index.html',context)
def detail(request,id):
    jost = get_object_or_404(Kurs,id=id)

    context={
        'jost': jost,

    }
    return render(request,'kurs/detail.html',context)

