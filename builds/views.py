from django.views.generic import CreateView, ListView
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Build
from .forms import BuildForm

# Create your views here.

class Builds(generic.ListView):
    """
    View/Display all builds in one place.
    """
    queryset = Build.objects.all()
    template_name = 'builds/builds.html'
    context_object_name = 'buildlist'


class AddBuild(LoginRequiredMixin, CreateView):
    """ 
    A class view to add a lego build.
    """
    template_name = 'builds/add_build.html'
    model = Build
    form_class = BuildForm
    success_url = "/builds/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBuild, self).form_valid(form)