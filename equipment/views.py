from equipment.models import Equipment
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404

# Create your views here.
def pc_map(request, *args, **kwargs):
    return HttpResponse("<h1>What ever</h1>")

def equipment_detail_view(requiest,pk):
    try:
        obj = Equipment.objects.get(pk=pk)
    except:
        raise Http404

    return HttpResponse(f"Computer id {obj,pk}")
    
