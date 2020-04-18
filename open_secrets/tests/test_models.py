import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestInsert:

    def test_insert_legislator(self):
        obj = mixer.blend('open_secrets.Legislator')
        assert obj.pk == 1, 'Should save an instance'
