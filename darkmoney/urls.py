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

from open_secrets.views import add_legislators, add_organization, LegislatorView, OrganizationView, index, LegislatorListView
from open_secrets.models import Legislator, Organization
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('legislator', LegislatorView.as_view(), name='legislator' ),
    path('legislators', LegislatorListView.as_view(), name='legislator_list'),
    path('organization', OrganizationView.as_view(), name='organization'),
    path('legislator/<str:pk>', LegislatorView.as_view(), name='get_legislator' ),
    path('organization/<str:pk>', OrganizationView.as_view(), name='get_organization'),
    path('add/legislators', add_legislators, name='add_legislators'),
    path('add/organizations', add_organization, name='add_organizations'),
]
