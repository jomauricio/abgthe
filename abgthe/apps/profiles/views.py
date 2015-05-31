from .models import Profile
from .forms import ProfilesForm
from braces.views import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView, RedirectView
from django.core.urlresolvers import reverse

class ProfileDetailView(LoginRequiredMixin, DetailView):
    
    model = Profile
    form_class = ProfilesForm
    template_name = "profiles/profile_detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profile
    form_class = ProfilesForm
    template_name = 'profiles/profile_update.html'
    slug_field = "username"
    slug_url_kwarg = "username"

class ProfileRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("profiles:profile_detail",
                       kwargs={"username": self.request.user.username})
        