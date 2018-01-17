"""un URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blog_urls
from blog.api.urls import router as api_route
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from blog.views import UserCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', auth_views.login, {'template_name': 'account_temp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^sign-up/$', UserCreateView.as_view(), name='signup'),

    # Blog
    url(r'^blog/', include(blog_urls)),

    #API
    url(r'^api/', include(api_route.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
