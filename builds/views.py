from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from .models import Build, Review
from .forms import BuildForm, ReviewForm

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
    reviews = build.reviews.all().order_by("-review_date")
    review_amount = build.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.build = build
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review was submitted and awaiting approval'
            )

    review_form = ReviewForm()

    return render(
        request,
        "builds/build_view.html",
        {
            "build": build,
            "reviews": reviews,
            "review_amount": review_amount,
            "review_form": review_form
        },
    )


class UserBuildsView(LoginRequiredMixin, ListView):
    """
    Display a list of builds created by the logged-in user.

    **Context**

    ``mybuilds``
        A list of :model:`build.Build` instances created by the user.

    **Template:**

    :template:`builds/my_builds.html`
    """
    model = Build
    template_name = 'builds/my_builds.html'
    context_object_name = 'mybuilds'
    paginate_by = 3

    def get_queryset(self):
        """
        Return a queryset of builds created by the logged-in user,
        ordered by creation date in descending order.
        """
        return Build.objects.filter(
            user=self.request.user).order_by('-created_on')


class Builds(generic.ListView):
    """
    Display a list of all builds with search functionality.

    **Context**

    ``buildlist``
        A list of :model:`build.Build` instances.

    ``search_query``
        The search query entered by the user.

    ``search_initiated``
        Boolean indicating if a search has been initiated.

    ``no_results``
        Boolean indicating if the search returned no results.

    **Template:**

    :template:`builds/builds.html`
    """
    template_name = 'builds/builds.html'
    model = Build
    context_object_name = 'buildlist'
    paginate_by = 3

    def get_queryset(self):
        """
        Return a queryset of builds filtered by the search query.
        If no search query is provided, return all builds.
        """
        query = self.request.GET.get('search')
        if query:
            buildlist = self.model.objects.filter(
                Q(set_number__icontains=query)
            )
        else:
            buildlist = self.model.objects.all()
        return buildlist

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the context dictionary.
        """
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search', '')
        context['search_query'] = query
        context['search_initiated'] = bool(query)
        context[
            'no_results'] = self.get_queryset().count() == 0 and query != ''
        return context


class AddBuild(LoginRequiredMixin, CreateView):
    """
    Create a new build.

    **Context**

    ``form``
        An instance of :form:`build.BuildForm`.

    **Template:**

    :template:`builds/add_build.html`
    """
    template_name = 'builds/add_build.html'
    model = Build
    form_class = BuildForm
    success_url = "/builds/"

    def form_valid(self, form):
        """
        If the form is valid, assign the logged-in user to the build,
        save the form, and display a success message.
        """
        form.instance.user = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'{self.request.user} your build post was successfully submitted'
        )
        response = super().form_valid(form)
        return response


class EditBuild(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit an existing build.

    **Context**

    ``form``
        An instance of :form:`build.BuildForm`.

    **Template:**

    :template:`builds/edit_build.html`
    """
    template_name = "builds/edit_build.html"
    model = Build
    form_class = BuildForm
    success_url = '/builds/'

    def test_func(self):
        """
        Ensure that the logged-in user is the owner of the build.
        """
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        """
        If the form is valid, assign the logged-in user to the build,
        save the form, and display a success message.
        """
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            f'{self.request.user} your build post was successfully edited')
        return response


class DeleteBuild(LoginRequiredMixin, UserPassesTestMixin,
                  SuccessMessageMixin, DeleteView):
    """
    Delete an existing build.

    **Context**

    ``object``
        An instance of :model:`build.Build` to be deleted.

    **Template:**

    :template:`builds/confirm_delete.html`
    """
    model = Build
    success_url = "/builds/"
    success_message = 'Your build post was successfully deleted'

    def test_func(self):
        """
        Ensure that the logged-in user is the owner of the build.
        """
        return self.request.user == self.get_object().user
