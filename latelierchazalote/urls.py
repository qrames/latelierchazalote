"""latelierchazalote URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


from blog.views import IndexView, CourDeCouture, CostumesDeScenes, CreetionSurMesures, atelierDeCreetion



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),

    # from views.py :
    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^cour-de-couture/$', CourDeCouture.as_view(), name="cour-de-couture"),
    url(r'^costumes-de-scenes/$', CostumesDeScenes.as_view(), name="costumes-de-scenes"),
    url(r'^creetion-sur-mesures/$', CreetionSurMesures.as_view(), name="creetion-sur-mesures"),
    url(r'^atelier-de-creetion/$', atelierDeCreetion.as_view(), name="atelier-de-creetion"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
