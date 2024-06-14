from django.urls import path
from .views import AddBuild, Builds, DeleteBuild
from . import views


urlpatterns = [
    path("add/", AddBuild.as_view(), name="add_build"),
    path('', Builds.as_view(), name="builds"),
    path('<slug:slug>/', views.build_view, name='build_view'),
    path('delete/<slug:pk>/', DeleteBuild.as_view(), name='delete_build'),

]