from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from front_site.models import User
from custom_auth.forms import CreateUserForm


def password_change_done(request):
    return HttpResponseRedirect(reverse('front_site:index'))


class UserCreateView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('front_site:index')
