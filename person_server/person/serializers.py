from rest_framework.serializers import ModelSerializer
from rest_framework.fields import IntegerField
from person.models import Person


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'gender', 'birthdate']
    id = IntegerField(read_only=True)
