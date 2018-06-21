from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from newsletter import views as newsletter_views
from projectx import views as projectx_views
# from newsletter.forms import ExRegistrationForm
# from registration.backends.default.views import RegistrationView


urlpatterns = [
    url(r'^$', newsletter_views.home, name='home'),
    url(r'^contact/$', newsletter_views.contact, name='contact'),
    url(r'^about/$', projectx_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'accounts/register/$',
    #     RegistrationView.as_view(form_class = ExRegistrationForm),
    #     name = 'registration_register'),
    url(r'^createDefInfra1/', newsletter_views.createDefInfra1, name='createDefInfra1'),
    url(r'^createDefInfra2/', newsletter_views.createDefInfra2, name='createDefInfra2'),
    url(r'^createDefInfra3/', newsletter_views.createDefInfra3, name='createDefInfra3'),
    url(r'^createDefInfra4/', newsletter_views.createDefInfra4, name='createDefInfra4'),
    url(r'^deleteInfra1/', newsletter_views.deleteInfra1, name='deleteInfra1'),
    url(r'^deleteInfra2/', newsletter_views.deleteInfra2, name='deleteInfra2'),
    url(r'^deleteInfra3/', newsletter_views.deleteInfra3, name='deleteInfra3'),
    url(r'^deleteInfra4/', newsletter_views.deleteInfra4, name='deleteInfra4'),
    url(r'^user/', newsletter_views.user, name='user'),
    url(r'^defInf/', newsletter_views.defInf, name='defInf'),
    url(r'^cusInf_Basic/', newsletter_views.cusInf_Basic, name='cusInf_Basic'),
    url(r'^cusInf_NACL/', newsletter_views.cusInf_NACL, name='cusInf_NACL'),
    url(r'^cusInf_SG/', newsletter_views.cusInf_SG, name='cusInf_SG'),
    url(r'^cusInf_Instance/', newsletter_views.cusInf_Instance, name='cusInf_Instance'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
