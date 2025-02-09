from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:service_id>/", views.detail, name="detail"),
    path("<int:service_id>/polls/", views.polls, name="polls"),
    path("<int:service_id>/vote/", views.vote, name="vote"),
]