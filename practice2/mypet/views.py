from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mypet.models import MyPet


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "mypet/index.html")



def pet_list(request: HttpRequest) -> HttpResponse:
    qs = MyPet.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    context_data = {
        "pet_list": qs,
    }
    return render(request, "mypet/pet_list.html", context_data)


def pet_detail(request: HttpRequest, pk: int) -> HttpResponse:
    mypet = MyPet.objects.get(pk=pk)
    context_data = {
        "mypet": mypet,
    }
    return render(request, "mypet/pet_detail.html", context_data)