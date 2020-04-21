"""darkmoney URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

from open_secrets.views import add_legislators, org_summary, view_leg, LegislatorView
from open_secrets.models import Legislator, Organization
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_legislators, name='home'),
    path('legislator/<str:pk>', LegislatorView.as_view() ),
    path('add', add_legislators, name='add_legislators'),
    path('organization/<str:pk>', org_summary, name='organization'),
]
