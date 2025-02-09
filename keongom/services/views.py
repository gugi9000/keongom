from django.shortcuts import render, get_object_or_404

from .models import Service


def index(request):
    service_list = Service.objects.order_by("name_text")[:5]
    context = {
        "service_list": service_list,
    }
    return render(request, "services/index.html", context)


def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    polls = service.poll_set.order_by("-poll_date")[:5]
    return render(request, "services/detail.html", {"service": service, "poll:": polls})


def polls(request, service_id):
    response = "You're looking at the polls of service %s."
    return render(response % service_id)


def vote(request, service_id):
    return render("You're voting on question %s." % service_id)