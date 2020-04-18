
import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from django.http import Http404
from mock import patch
from django.core import mail
pytestmark = pytest.mark.django_db

from .. import views

class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        res = views.HomeView.as_view()(req)
        assert res.status_code == 200, 'Should be callable by anyone'


class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        res = views.AdminView.as_view()(req)
        assert 'login' in res.url, 'Should redirect to login'

    def test_superuser(self):
        user = mixer.blend('auth.User', is_superuser=True)
        req = RequestFactory().get('/')
        req.user = user
        res = views.AdminView.as_view()(req)
        assert res.status_code == 200, 'Should be callable by a is_superuser'
