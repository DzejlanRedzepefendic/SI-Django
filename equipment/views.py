from equipment.models import Equipment
from django.http import HttpResponse, JsonResponse,Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, redirect
# Create your views here.
@login_required
def pcmap_view(request):
    return render(request=request, template_name="pcmap.html")
