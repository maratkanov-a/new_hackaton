from django.conf.urls import url, include

from front_site.views import MainPage, CompanyCreateView, CompanyUpdateView, EventCreateView, EventDetailView, \
    event_subscribe

urlpatterns = [
    url(r'^$', MainPage.as_view(), name='index'),
    url(r'^company/create/$', CompanyCreateView.as_view(), name='company_create'),
    url(r'^company/my/(?P<pk>\d+)$', CompanyUpdateView.as_view(), name='company_update'),

    url(r'^event/create/$', EventCreateView.as_view(), name='event_create'),
    url(r'^event/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event_detail'),
    url(r'^event_subscribe/(?P<pk>\d+)/$', event_subscribe, name='event_subscribe'),
]
