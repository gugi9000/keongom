import json

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Service


def index(request):
    service_list = Service.objects.filter(poll__isnull=False).distinct().order_by("name_text")
    context = {
        "service_list": service_list,
    }
    return render(request, "services/index.html", context)


def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    polls = service.poll_set.order_by("-poll_date")[:5]
    return render(request, "services/detail.html", {"service": service, "pols:": polls})


def polls(request, service_id):
    response = "You're looking at the polls of service %s."
    return render(response % service_id)

def json(request): ## Return a JSON response with enabled services and their latest poll status and poll date
    service_list = Service.objects.filter(poll__isnull=False).distinct().order_by("name_text")
    # response = serializers.serialize("json", service_list)
    response = []
    for service in service_list:
        latest_poll = service.poll_set.order_by("-poll_date").first()
        response.append({
            "name_text": service.name_text,
            "url_text": service.url_text,
            "status_code": latest_poll.status_code if latest_poll else None,
            "poll_date": latest_poll.poll_date if latest_poll else None,
        })
    return JsonResponse(response, safe=False)