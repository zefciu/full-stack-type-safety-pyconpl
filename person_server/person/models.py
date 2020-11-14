from django.db import models

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'X', 'Male'


class Person(models.Model):
    first_name = models.CharField(max_length=128, null=True, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    birthdate = models.DateField(blank=False, null=False)

    @property
    def full_name(self) -> str:
        if self.first_name is None:
            return self.last_name
        return ' '.join([self.first_name, self.last_name])

