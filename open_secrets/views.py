from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, UpdateView, View, ListView, DetailView
from django.views import  generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, request, response
from django.core.mail import send_mail
from django.shortcuts import redirect
# Create your views here.

from django.conf import settings
import requests
from django.urls import reverse

from . serializer import LegislatorSerializer, OrganizationSerializer
from . forms import SubmitLegislator, AddOrganization
from . models import *


class LegislatorView(generic.DetailView):
    template_name = 'legislator.html'
    model = Legislator

class LegislatorListView(generic.ListView):
    template_name = 'legislator_list.html'
    model = Legislator

class OrganizationView(generic.DetailView):
    template_name = 'organization.html'
    model = Organization

def index(request):

    num_leg = Legislator.objects.all().count()
    context = {
        'num_leg': num_leg,
    }

    return render(request, 'index.html', context=context)

def add_legislators(request):
    """
    This view handles the adding of one or several legislators. If attempting
    to add multiple legislators (e.g., all legislators from South Carolina),
    the response object's ['legislator'] attribute will be a list which is
    not the case when adding a single legislator. Thus, this view handles
    the construction of a custom response object so that single and multiple
    legislator additions can be handled in the same way.
    """
    if request.method == "POST":
        form = SubmitLegislator(request.POST)
        if form.is_valid():
            cid = form.cleaned_data['cid']

            payload = {'id': cid, 'apikey': settings.OPEN_SECRETS_KEY, 'output': 'json'}
            r = requests.get('http://www.opensecrets.org/api/?method=getLegislators', params=payload)
            json = r.json()

            legislators = json['response']['legislator']
            validation_queue = []
            response = { 'legislators' : [] }

            single_legislator = len(legislators) == 1

            if single_legislator:
                legislator = json['response']['legislator']['@attributes']
                validation_queue.append(legislator)
            else:
                for i in range(len(legislators)):
                    legislator = legislators[i]['@attributes']
                    validation_queue.append(legislator)
                    return redirect(reverse('legislator', kwargs={'pk': legislator.cid}))
            for legislator in validation_queue:
                serializer = LegislatorSerializer(data=legislator)
                if serializer.is_valid():
                    legislator = serializer.save()
                    response['legislators'].append({'legislator': legislator})
                else:
                    print(serializer.errors)
                    return None


            return render(request, 'legislator_list.html', {'form': form, 'legislators': response['legislators']})
            #)

    else:
        form = SubmitLegislator()

    return render(request, 'legislator_list.html', {'form': form})


def add_organization(request):

    if request.method == "POST":
        form = AddOrganization(request.POST)
        if form.is_valid():
            id = form.cleaned_data['orgid']

            payload = {'id': id, 'apikey': settings.OPEN_SECRETS_KEY, 'output': 'json'}
            r = requests.get('http://www.opensecrets.org/api/?method=orgSummary', params=payload)
            json = r.json()

            org = json['response']['organization']

            serializer = OrganizationSerializer(data=org['@attributes'])
            if serializer.is_valid():
                organization = serializer.save()
                return redirect(reverse('organization', kwargs={'pk': organization.orgid}))
            else:
                print(serializer.errors)

    else:
        form = GetOrganization(request.GET)

    return render(request, 'organization.html', {'form': form })


class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    # override dispatch functions
    @method_decorator(login_required)
    def dispatch(self, req, *args, **kwargs):
        return super(AdminView, self).dispatch(req, *args, **kwargs)
