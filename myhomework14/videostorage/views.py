from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from videostorage.models import Video


index = ListView.as_view(model=Video, template_name="videostorage/index.html")


def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    return render(
        request,
        "videostorage/video_detail.html",
        {
            "video": video,
        },
    )