from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Entity
from .models import Info

# Create your views here.
def index(request):
    context = {"entitys": Entity.objects.all()}
    return render(request, "polls/index.html", context)

def location(request):
    context = {"infos": Info.objects.all()}
    return render(request, "polls/location.html", context)

def detail(request, entity_id):
    context = {"entity": Entity.objects.get(pk=entity_id)}
    return render(request, "polls/entity.html", context)

def locate(request, info_id):
    context = {"location_of": Info.objects.get(pk=info_id).entity, "info": Info.objects.get(pk=info_id)}
    return render(request, "polls/locationOf.html", context)

def results(request, entity_id):
    q = Entity.objects.get(pk=entity_id)
    return HttpResponse(f"{q.entity_text} results page")