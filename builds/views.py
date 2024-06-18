from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
) 
from .models import Build
from .forms import BuildForm

# Create your views here.

def build_view(request, slug):
    """
    Display an individual :model:`build.Build`.

    **Context**

    ``post``
        An instance of :model:`build.Build`.

    **Template:**

    :template:`builds/build_view.html`
    """

    queryset = Build.objects.all()
    build = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "builds/build_view.html",
        {"build": build },
    )

class Builds(generic.ListView):
    """
    View/Display all builds in one place.

    Provides search functionality for model numbers. 
    If a model number is a match, this will display.

    """

    queryset = Build.objects.all()
    template_name = 'builds/builds.html'
    model = Build
    context_object_name = 'buildlist'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('search')
        if query:
            buildlist = self.model.objects.filter(
                Q(set_number__icontains=query)
            )
        else:
            buildlist = Build.objects.all()

        return buildlist

    


class AddBuild(LoginRequiredMixin, CreateView):
    """ 
    A class view to add a Lego build.
    """
    template_name = 'builds/add_build.html'
    model = Build
    form_class = BuildForm
    success_url = "/builds/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'{self.request.user} your build post was succesfully submitted'
        )
        response = super().form_valid(form)
        return response


class EditBuild(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a build form/post"""
    template_name = "builds/edit_build.html"
    model= Build
    form_class = BuildForm
    success_url = '/builds/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, f'{self.request.user} your build post was succesfully edited')
        return response


class DeleteBuild(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    Delete a lego build post.
    """
    model = Build
    success_url = "/builds/"
    success_message = 'Your build post was succesfully deleted'

    def test_func(self):
        return self.request.user == self.get_object().user


