from django_cron import CronJobBase, Schedule
from .models import Summoners

def my_scheduled_job():
      pass

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = '.liigade_kutsumine4'    # a unique code

    def do(self):
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



