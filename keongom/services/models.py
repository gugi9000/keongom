import datetime

from django.utils import timezone
from django.db import models


class Service(models.Model):
    name_text = models.CharField(max_length=200)
    url_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    enabled_toggle = models.BooleanField()
    tls_toggle = models.BooleanField()
    
    def __str__(self):
        return self.name_text


class Poll(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    poll_date = models.DateTimeField("date polled")
    status_code = models.IntegerField(default=0)

    def __str__(self):
        return self.service.name_text + " - " + str(self.status_code) + " + " + str(self.poll_date)
    
    def was_polled_recently(self):
        return self.poll_date >= timezone.now() - datetime.timedelta(days=14)
    
    class Meta:
        get_latest_by = "poll_date"
        ordering = ["-poll_date"]

## TODO - Add a model for certificates information