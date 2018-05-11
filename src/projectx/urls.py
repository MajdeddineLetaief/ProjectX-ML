from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from newsletter import views as newsletter_views
from projectx import views as projectx_views

urlpatterns = [
    url(r'^$', newsletter_views.home, name='home'),
    url(r'^contact/$', newsletter_views.contact, name='contact'),
    url(r'^about/$', projectx_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^createInfra/', newsletter_views.createInfra, name='createInfra'),
    url(r'^deleteInfra/', newsletter_views.deleteInfra, name='deleteInfra'),
    url(r'^user/', newsletter_views.user, name='user'),
    url(r'^defInf/', newsletter_views.defInf, name='defInf'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
