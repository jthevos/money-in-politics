from django import forms

class SubmitLegislator(forms.Form):
    cid = forms.CharField()


class GetOrganization(forms.Form):
    orgid = forms.CharField()
