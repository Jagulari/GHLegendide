from __future__ import absolute_import
from celery.task import PeriodicTask
from .liigade_kutsumine4 import add
from datetime import timedelta
from celery import task

from lolPy import RiotApiClient
import time
from .models import Summoners
from celery import shared_task
from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//') #!

import os
os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "proj.settings"

#@celery.task()
#class addTask(PeriodicTask):
#    run_every = timedelta(minutes=1)
#
#    def run(self, **kwargs):
#        add()

from .models import Summoners
@EEtabel.task()
def add():
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