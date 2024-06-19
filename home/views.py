from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    """
    Class based view to render home page.
    """
    template_name = 'home/index.html'
