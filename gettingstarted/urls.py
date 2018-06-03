from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^resume/$', TemplateView.as_view(template_name='resume.html'),
        name='resume'),
    url(r'^projects/$', TemplateView.as_view(template_name='tba.html'),
        name='tba.html'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("posts.urls", namespace="blog")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
