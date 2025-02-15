from django.urls import path

from . import views

app_name = "service"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:service_id>/", views.detail, name="detail"),
    path("<int:service_id>/polls/", views.polls, name="polls"),
    path("all.json", views.json, name="json"),  
]