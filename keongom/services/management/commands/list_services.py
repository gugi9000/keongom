from django.core.management.base import BaseCommand, CommandError
from services.models import Service

class Command(BaseCommand):
    help = "List all services"

    def handle(self, *args, **options):
        services = Service.objects.all()
        for service in services:
            self.stdout.write(self.style.SUCCESS(service.name_text))
            self.stdout.write(f"  URL: {service.url_text}")
            self.stdout.write(f"  Description: {service.description_text}")
            self.stdout.write(f"  Enabled: {service.enabled_toggle}")
            self.stdout.write(f"  TLS: {service.tls_toggle}")
            self.stdout.write("")
            