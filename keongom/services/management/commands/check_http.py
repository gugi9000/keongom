import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from services.models import Service, Poll

class Command(BaseCommand):
    help = "Check all services"

    def handle(self, *args, **options):
        check_services()


def check_services():
    services = Service.objects.all()
    for service in services:
        if service.enabled_toggle:
            try:
                response = requests.get(service.url_text, timeout=5)
                status_code = response.status_code
            except requests.exceptions.RequestException as e:
                status_code = 0
            poll = Poll(service=service, poll_date=timezone.now(), status_code=status_code)
            poll.save()
            print(f"Polled {service.name_text} - {status_code}")
        else:
            print(f"Service {service.name_text} is disabled")