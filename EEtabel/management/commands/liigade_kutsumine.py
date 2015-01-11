from django.core.management.base import BaseCommand
from django.conf import settings
from EEtabel.models import Summoners
from polls.models import MyModel
from lolPy import RiotApiClient
import time


list_of_summoner_names = list(MyModel.objects.values_list('title', flat=True))
key = "b607eef2-c0ca-403b-b7af-6a1343574766"
client = RiotApiClient.RiotApiClient(key, "euw")

class Command(BaseCommand):

    def handle(self, *args, **options):
        Summoners.objects.all().delete()
        kaks = client.search(list_of_summoner_names)
        for x in list_of_summoner_names:
            ranking = Summoners.objects.create(
                Summoner_name=kaks.name,
                League=client.league_data()[0].tier,
                Division=client.league_data()[0].entries[0].division,
                League_points=client.league_data()[0].entries[0].leaguePoints)
            kaks = client.next()
            time.sleep(4)
