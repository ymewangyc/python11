"""cmdb URL Configuration

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
from .views import hello
from . import testdb
from .search import search,search_form
from .search2 import search_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello),
    url(r'^add$', testdb.add),
    url(r'^chaxun$', testdb.chaxun),
    url(r'^xiugai$', testdb.change),
    url(r'^del$', testdb.shanchu),
    url(r'^search-form$', search_form),
    url(r'^search$', search),
    url(r'^search-post$', search_post),
    url(r'^look$', testdb.chaxun),
]
