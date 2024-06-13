from django.urls import path
from .views import AddBuild, Builds


urlpatterns = [
    path("add/", AddBuild.as_view(), name="add_build"),
    path('', Builds.as_view(), name="builds")
]