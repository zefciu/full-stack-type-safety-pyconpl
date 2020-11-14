from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'


class Person(models.Model):
    first_name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    birthdate = models.DateField(blank=False, null=False)

    @property
    def full_name(self) -> str:
        return ' '.join([self.first_name, self.last_name])

