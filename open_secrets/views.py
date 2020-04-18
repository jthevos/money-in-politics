from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
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


from .serializer import LegislatorSerializer


import requests
from . forms import SubmitLegislator
from . import models



def save_embed(request):

    if request.method == "POST":
        form = SubmitLegislator(request.POST)
        if form.is_valid():
            cid = form.cleaned_data['cid']

            payload = {'id': cid, 'apikey': settings.OPEN_SECRETS_KEY, 'output': 'json'}
            r = requests.get('http://www.opensecrets.org/api/?method=getLegislators', params=payload)
            json = r.json()

            legislators = json['response']['legislator']
            response = {'legislators' : []}

            if len(legislators) == 1:
                print(legislators['@attributes'])
                serializer = LegislatorSerializer(data=legislators['@attributes'])
                print('is valid ??? ', serializer.is_valid())
                if serializer.is_valid():
                    legislator = serializer.save()
                    response['legislators'].append({'legislator': legislator})
                    #print('response ==== ', response['legislators'])
                    print({legislator})
                    #return render(request, 'legislator.html', {'legislators': {legislator}})
                    return render(request, 'legislator.html', {'legislators': response['legislators']})
                else:
                    print(serializer.errors)

            else:
                for i in range(len(legislators)):
                    print(legislators[i]['@attributes'])
                    print('\n')
                    serializer = LegislatorSerializer(data=legislators[i]['@attributes'])
                    if serializer.is_valid():
                        legislator = serializer.save()
                        response['legislators'].append({'legislator': legislator})

                    else:
                        print(serializer.errors)

                #print(legislatorz)
                tempList = response['legislators']
                print(tempList)
                return render(request, 'legislator.html', {'legislators': tempList})

    else:
        form = SubmitLegislator()

    return render(request, 'index.html', {'form': form})
#
# class HomeView(TemplateView):
#     template_name = 'open_secrets/home.html'
#
#     def save_embed(request):
#
#         if request.method == "POST":
#             form = SubmitEmbed(request.POST)
#             if form.is_valid():
#                 url = form.cleaned_data['url']
#                 r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
#                 json = r.json()
#                 serializer = EmbedSerializer(data=json)
#                 if serializer.is_valid():
#                     embed = serializer.save()
#                     return render(request, 'embeds.html', {'embed': embed})
#         else:
#             form = SubmitEmbed()
#
#         return render(request, 'index.html', {'form': form})
#     # request.query_params


class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    # override dispatch functions
    @method_decorator(login_required)
    def dispatch(self, req, *args, **kwargs):
        return super(AdminView, self).dispatch(req, *args, **kwargs)
