from django.db import models


from django.core import serializers

# for obj in serializers.deserialize("xml", data):
#     dir(obj)
class Legislator(models.Model):
    cid = models.CharField(max_length=10)
    firstlast = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=200, default='')
    party = models.CharField(max_length=1, default='I')
    office = models.CharField(max_length=200, default='')
    gender = models.CharField(max_length=1, default='X')
    first_elected = models.CharField(max_length=200, default='')
    exit_code = 0
    comments = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, default='', blank=True)
    fax = models.CharField(max_length=200, default='', blank=True)
    website = models.CharField(max_length=200, default='', blank=True)
    webform = models.CharField(max_length=200, default='', blank=True)
    congress_office = models.CharField(max_length=200, default='', blank=True)
    bioguide_id = models.CharField(max_length=200, default='', blank=True)
    votesmart_id = models.CharField(max_length=200, default='', blank=True)
    feccandid = models.CharField(max_length=200, default='',blank=True)
    twitter_id = models.CharField(max_length=200, default='', blank=True)
    youtube_url = models.CharField(max_length=200, default='', blank=True)
    facebook_id = models.CharField(max_length=200, default='', blank=True)
    birthdate = models.CharField(max_length=200, default='', blank=True)

#{'cid': 'N00041400', 'firstlast': 'Joe Cunningham', 'lastname': 'Cunningham', 'party': 'D', 'office': 'SC01', 'gender': 'M', 'first_elected': '2018', 'exit_code': '0', 'comments': '', 'phone': '202-225-3176', 'fax': '', 'website': 'https://cunningham.house.gov/', 'webform': '', 'congress_office': '423 Cannon House Office Building', 'bioguide_id': 'C001122', 'votesmart_id': '', 'feccandid': '', 'twitter_id': 'RepCunningham', 'youtube_url': '', 'facebook_id': '', 'birthdate': '1982-05-26'}

# class PersonalFinanceRecord(models.Model):
#     pass
