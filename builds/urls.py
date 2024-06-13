from django.urls import path
from .views import AddBuild


urlpatterns = [
    path("add/", AddBuild.as_view(), name="add_build"),
]