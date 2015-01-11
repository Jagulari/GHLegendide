import sys
from os import path
import collections
import datetime
from models import Summoners
from wsgi.openshift.lolPy import RiotApiClient
from django.core.management import call_command
from models import *
from wsgi.openshift import settings


list_of_summoner_names = ['jagular1', 'mine06', 'devil2g', 'insener',
                          'kim27', 'tulnukawara']
key = "b607eef2-c0ca-403b-b7af-6a1343574766"
client = RiotApiClient.RiotApiClient(key, "euw")
summoner = client.search(list_of_summoner_names)


def Summoners():
    for x in list_of_summoner_names:
        ranking = Summoners.objects.create(
            Summoner_name=summoner.name,
            League=client.league_data([0].tier),
            Division=client.league_data([0].entries[0].division),
            League_points=client.league_data([0].entries[0].leaguePoints),
            summoner=client.next())
        ranking.save()
