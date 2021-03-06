from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    nationality = models.ManyToManyField('countries.Country', related_name='person')
    father = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return '{}'.format(self.first_name)
