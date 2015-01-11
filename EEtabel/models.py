from django.db import models
import django_tables2 as tables
from lolPy import RiotApiClient
import time
from django.db.models import Sum
from django.conf import settings
if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'ENGINE': 'django.db.backends.sqlite3',
                # Or path to database file if using sqlite3.
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=("runnable", )
    )

class Summoners(models.Model):

    VALUES = {
        'BRONZE': 0,
        'SILVER': 500,
        'GOLD': 1000,
        'PLATINUM': 1500,
        'DIAMOND': 2000,
        'MASTER': 2500,
        'CHALLENGER': 3000,
        'V': 0,
        'IV': 100,
        'III': 200,
        'II': 300,
        'I': 400,
    }

    Summoner_name = models.CharField(max_length=25, unique=False)
    League = models.CharField(max_length=20, )
    Division = models.CharField(max_length=5, )
    League_points = models.DecimalField(max_digits=3, decimal_places=0)
    TotalLP = models.PositiveIntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        self.TotalLP = self.calculate_sum()
        super(Summoners, self).save(*args, **kwargs)

    def calculate_sum(self):
        try:
            value_a = self.VALUES.get(self.League, 0)
            value_b = self.VALUES.get(self.Division, 0)
            value_c = self.League_points
            return value_a + value_b + value_c
        except KeyError:
            return 0


    def __str__(self):
        return ' '.join([
            self.Summoner_name,
            self.League,
            self.Division,
            ])