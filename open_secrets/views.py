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

from xml.etree import ElementTree


from .serializer import LegislatorSerializer, OrganizationSerializer


import requests
from . forms import SubmitLegislator, GetOrganization
from . import models


class LegislatorView(generic.DetailView):
    template_name = 'legislator.html'
    model = models.Legislator

class OrganizationView(generic.DetailView):
    template_name = 'organization.html'
    model = models.Legislator


def add_legislators(request):

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

            multiple_legislators = len(legislators) != 1

            if not multiple_legislators:
                legislator = json['response']['legislator']['@attributes']
                validation_queue.append(legislator)
            else:
                for i in range(len(legislators)):
                    legislator = legislators[i]['@attributes']
                    validation_queue.append(legislator)
            print(legislators)

            for legislator in validation_queue:

                #serializer = LegislatorSerializer(data=legislators['@attributes'])
                serializer = LegislatorSerializer(data=legislator)
                if serializer.is_valid():
                    legislator = serializer.save()
                    response['legislators'].append({'legislator': legislator})
                else:
                    print('The error is in the serializer')
                    print(serializer.errors)


            return render(request, 'legislator_list.html', {'form': form, 'legislators': response['legislators']})


            # if len(legislators) == 1:
            #     serializer = LegislatorSerializer(data=legislators['@attributes'])
            #     if serializer.is_valid():
            #         legislator = serializer.save()
            #         response['legislators'].append({'legislator': legislator})
            #         return render(request, 'legislator.html', {'form': form, 'legislators': response['legislators']})
            #     else:
            #         print(serializer.errors)
            # else:
            #     for i in range(len(legislators)):
            #         serializer = LegislatorSerializer(data=legislators[i]['@attributes'])
            #         if serializer.is_valid():
            #             legislator = serializer.save()
            #             response['legislators'].append({'legislator': legislator})
            #         else:
            #             print(serializer.errors)
            #
            #     return render(request, 'legislator.html', {'form': form, 'legislators': response['legislators']})

    else:
        form = SubmitLegislator()

    return render(request, 'index.html', {'form': form})



def org_summary(request):

    if request.method == "POST":
        form = GetOrganization(request.POST)
        if form.is_valid():
            id = form.cleaned_data['orgid']

            payload = {'id': id, 'apikey': settings.OPEN_SECRETS_KEY, 'output': 'json'}
            r = requests.get('http://www.opensecrets.org/api/?method=orgSummary', params=payload)
            json = r.json()

            org = json['response']['organization']

            serializer = OrganizationSerializer(data=org['@attributes'])
            if serializer.is_valid():
                organization = serializer.save()
                return render(request, 'organization.html', {'form': form, 'organization': org})
            else:
                print(serializer.errors)


    else:
        form = GetOrganization()

    return render(request, 'organization.html', {'form': form })


def view_leg(request):
    return get_object_or_404(models.Legislator, cid='N00007360')

class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    # override dispatch functions
    @method_decorator(login_required)
    def dispatch(self, req, *args, **kwargs):
        return super(AdminView, self).dispatch(req, *args, **kwargs)
