"""corals_project URL Configuration

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


	#url(r'^about/$', views.AboutPageView.as_view(), name="about"), #Add this /about/ route
	#url(r'^search/$', views.SearchPageView.as_view(), name="search"),
	#url(r'^coraltemplate/$', views.CoralTemplatePageView.as_view(), name="coraltemplate"),

"""
from django.conf.urls import url
from django.contrib import admin
from corals_app import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^about/$', views.AboutPageView.as_view(), name="about"),
	url(r'^search/$', views.SearchPageView.as_view(), name="search"),
	url(r'^coraltemplate/$', views.coral_detail, name="coraltemplate"),


]
