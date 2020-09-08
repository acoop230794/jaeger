from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("location/", views.location, name="location"),
    path("<int:entity_id>/", views.detail, name="detail"),
    path("location/<int:info_id>/", views.locate, name="locate"),
    path("<int:entity_id>/results", views.results, name="results"),
]