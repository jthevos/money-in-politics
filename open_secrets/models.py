from django.db import models


from django.core import serializers

# for obj in serializers.deserialize("xml", data):
#     dir(obj)
class Legislator(models.Model):
    cid             = models.CharField(max_length=10, primary_key=True)
    firstlast       = models.CharField(max_length=100, default='')
    lastname        = models.CharField(max_length=200, default='')
    party           = models.CharField(max_length=1, default='I')
    office          = models.CharField(max_length=200, default='')
    gender          = models.CharField(max_length=1, default='X')
    first_elected   = models.CharField(max_length=200, default='')
    exit_code       = 0
    comments        = models.CharField(max_length=200, blank=True)
    phone           = models.CharField(max_length=200, default='', blank=True)
    fax             = models.CharField(max_length=200, default='', blank=True)
    website         = models.CharField(max_length=200, default='', blank=True)
    webform         = models.CharField(max_length=200, default='', blank=True)
    congress_office = models.CharField(max_length=200, default='', blank=True)
    bioguide_id     = models.CharField(max_length=200, default='', blank=True)
    votesmart_id    = models.CharField(max_length=200, default='', blank=True)
    feccandid       = models.CharField(max_length=200, default='', blank=True)
    twitter_id      = models.CharField(max_length=200, default='', blank=True)
    youtube_url     = models.CharField(max_length=200, default='', blank=True)
    facebook_id     = models.CharField(max_length=200, default='', blank=True)
    birthdate       = models.CharField(max_length=200, default='', blank=True)

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    def create(self, **kwargs):
        try:
            print('in try block')
            return Legislator.objects.get(**kwargs)
        except:
            print('in except block')
            return Legislator.objects.create(**kwargs)

    def __str__(self):
        return self.firstlast

    class Meta:
        managed = True


# class LegislatorManager(models.Manager):
#
#     def create(self, **kwargs):
#         try:
#             return Legislator.objects.get(**kwargs)
#         except:
#             return Legislator.objects.create(**kwargs)


class Organization(models.Model):
    orgid         = models.CharField(max_length=10, primary_key=True)
    orgname       = models.CharField(max_length=100, default='')
    total         = models.CharField(max_length=200, default='')
    indivs        = models.CharField(max_length=1, default='I')
    pacs          = models.CharField(max_length=200, default='')
    soft          = models.CharField(max_length=1, default='X')
    tot527        = models.CharField(max_length=200, default='')
    dems          = models.CharField(max_length=200, default='')
    repubs        = models.CharField(max_length=200, blank=True)
    lobbying      = models.CharField(max_length=200, default='', blank=True)
    outside       = models.CharField(max_length=200, default='', blank=True)
    mems_invested = models.CharField(max_length=200, default='', blank=True)
    gave_to_pac   = models.CharField(max_length=200, default='', blank=True)
    gave_to_party = models.CharField(max_length=200, default='', blank=True)
    gave_to_527   = models.CharField(max_length=200, default='', blank=True)
    gave_to_cand  = models.CharField(max_length=200, default='', blank=True)

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]
        
    def __str__(self):
        return self.orgname

    class Meta:
        managed = True
