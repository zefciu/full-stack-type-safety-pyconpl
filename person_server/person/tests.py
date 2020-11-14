import datetime

from django.test import TestCase
from django_swagger_tester.testing import validate_response

from person.models import Person, Gender

# Create your tests here.
class TestPerson(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            first_name = 'John',
            last_name = 'Smith',
            gender = Gender.MALE,
            birthdate = datetime.date(1982, 3, 29)
        )
        self.null_person = Person.objects.create(
            first_name = None,
            last_name = 'Smith',
            gender = Gender.MALE,
            birthdate = datetime.date(1982, 3, 29)
        )

    def test_person_get(self):
        path = f'/api/person/{self.person.id}/'
        resp = self.client.get(path)
        validate_response(
            response = resp,
            method='GET',
            route='/api/person/{personId}',
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['first_name'], 'John')

    def test_null_person_get(self):
        path = f'/api/person/{self.person.id}/'
        resp = self.client.get(path)
        validate_response(
            response = resp,
            method='GET',
            route='/api/person/{personId}',
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['first_name'], None)
