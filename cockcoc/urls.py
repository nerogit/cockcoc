"""cockcoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from app.views import (
    BarDetail,
    BarList,
    CocktailDetail,
    CocktailList,
    login,
    register,
    index,
    select_tags,
    BarViewSet
)

from django.contrib import admin
from cockcoc.settings import MEDIA_ROOT, MEDIA_URL

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bars', BarViewSet)

urlpatterns = [
    url(r'^$', index),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^bars/$', BarList.as_view(), name='bar_list'),
    url(r'^bars/(?P<pk>\d+)$', BarDetail.as_view(), name='bar_detail'),

    url(r'^cocktails/$', CocktailList.as_view(), name='cocktail_list'),
    url(r'^cocktails/(?P<pk>\d+)$', CocktailDetail.as_view(), name='cocktail_detail'),

    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^select_tag/$', select_tags),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
