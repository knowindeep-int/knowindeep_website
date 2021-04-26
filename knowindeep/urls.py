"""knowindeep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler404, handler400, handler500

from settings import base as settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = "project.views.error404"
handler400 = "project.views.error400"
handler500 = "project.views.error500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teach/', include('teach.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('site/user/',include('site_users.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('site/api/',include('api.urls')),
    re_path("^[@](?P<slug>[-\w]+)/",include('author.urls')),
    path('blogs/',include('blogs.urls')),
    path('',include('project.urls')),
    path('oauth/',include('social_django.urls'),name='social'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  