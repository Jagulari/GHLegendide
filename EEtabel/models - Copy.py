from django.db import models
import django_tables2 as tables
from lolPy import RiotApiClient
import time
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
    Summoner_name = models.CharField(max_length=25, unique=True)
    League = models.CharField(max_length=20, )
    Division = models.CharField(max_length=5, )
    League_points = models.CharField(max_length=5, )

    def __str__(self):
        return ' '.join([
            self.Summoner_name,
            self.League,
            self.Division,
            self.League_points,
        ])

class SimpleTable(tables.Table):
    class Meta:
        model = Summoners
#Töötab!
list_of_summoner_names = ['mine06', 'devil2g', 'jagular1', 'kim27', 'tulnukawara', 'ped1gree' ]
key = "b607eef2-c0ca-403b-b7af-6a1343574766"
client = RiotApiClient.RiotApiClient(key, "euw")
kaks = client.search(list_of_summoner_names)

for i in list_of_summoner_names:

    ranking = Summoners.objects.create(
        Summoner_name=kaks.name,
        League=client.league_data()[0].tier,
        Division=client.league_data()[0].entries[0].division,
        League_points=client.league_data()[0].entries[0].leaguePoints)
    time.sleep(2)
    kaks = client.next()

