from django.urls import path
from .views import AddBuild, Builds, DeleteBuild, EditBuild
from . import views


urlpatterns = [
    path("add/", AddBuild.as_view(), name="add_build"),
    path('', Builds.as_view(), name="builds"),
    path('<slug:slug>/', views.build_view, name='build_view'),
    path("edit/<slug:pk>/", EditBuild.as_view(), name="edit_build",),
    path('delete/<slug:pk>/', DeleteBuild.as_view(), name='delete_build'),
]
