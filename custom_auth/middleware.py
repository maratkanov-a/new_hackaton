from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class AuthCheckerMiddleware(object):
    allowed_urls = [reverse('login')]

    def process_request(self, request):
        # if 'api' in request.path:
        #     return None
        # elif not request.user.is_authenticated() and request.path not in self.allowed_urls:
        #     return HttpResponseRedirect(reverse('login'))
        # else:
            return None
