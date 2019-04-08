from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from events.models import Eventa
from django.core.paginator import Paginator
from django.db.models import Q
def index(request):
    events_list = Eventa.objects.all()
    context = {
        'events_list':events_list,
    }

    return render(request,'events/index.html',context)

def detail(request,id):
    sost = get_object_or_404(Eventa,id=id)

    context={
        'sost': sost,

    }
    return render(request,'events/detail.html',context)