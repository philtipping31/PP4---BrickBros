from django.views.generic import CreateView, ListView
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

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
    """
    queryset = Build.objects.all()
    template_name = 'builds/builds.html'
    context_object_name = 'buildlist'
    paginate_by = 3


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
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, f'{self.request.user} your post was submitted')
        return response