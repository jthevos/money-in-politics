from django import forms

class SubmitLegislator(forms.Form):
    cid = forms.CharField()

class GetOrganization(forms.Form):
    orgid = forms.CharField()

class AddOrganization(forms.Form):
    orgid = forms.CharField()

class SearchOrganizations(forms.Form):
    orgname = forms.CharField(min_length=1)
