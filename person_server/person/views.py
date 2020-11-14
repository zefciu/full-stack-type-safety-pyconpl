from rest_framework.viewsets import ModelViewSet

from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
