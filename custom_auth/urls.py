from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from custom_auth import views
from custom_auth.forms import LoginForm

urlpatterns = [
    url('^login/$', auth_views.login, {"template_name": "login.html", "form_class": LoginForm}, name='login'),
    url('^logout/$', auth_views.logout, {'next_page': reverse_lazy('index')}, name='logout'),
    url('^change-password/', auth_views.password_change, {"template_name": "change_password.html"}, name='password-change'),
    url('^change-password-done/', views.password_change_done, name='password_change_done'),
    url('^registration/$', views.UserCreateView.as_view(), name='registration'),

]
