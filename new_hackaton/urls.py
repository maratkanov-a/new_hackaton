from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from new_hackaton import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('front_site.urls', namespace='front_site')),
    url('^', include('custom_auth.urls')),
    url(r'api/^', include('api.urls', namespace='api')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
