"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from filebrowser.sites import site as filebrowser_site

filebrowser_site.directory = "uploads/"
# For development
filebrowser_patterns = static(
    settings.FILEBROWSER_URL,
    document_root=settings.FILEBROWSER_DIRECTORY
)
filebrowser_versions_patterns = static(
    settings.FILEBROWSER_VERSIONS_URL,
    document_root=settings.FILEBROWSER_VERSIONS_BASEDIR
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('chat/', include("chat.urls")),
    path('polls/', include('polls.urls')),

    # the following two are for file browser, must come before /admin
    path('admin/filebrowser/', filebrowser_site.urls),
    path('grappelli/', include('grappelli.urls')),

    path('admin/', admin.site.urls),
] + filebrowser_patterns + filebrowser_versions_patterns
