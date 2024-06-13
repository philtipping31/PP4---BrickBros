from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Build
from .forms import BuildForm

# Create your views here.

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