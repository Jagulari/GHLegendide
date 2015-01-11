from django.db import connection, transaction
from celery.task.schedules import crontab
from celery.decorators import periodic_task

cursor = connection.cursor()
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def te():
    cursor.execute("""INSERT INTO EEtabel_summoners ('Summoner_name', 'League', 'Division', 'League_points') VALUES (?, ?, ?, ?)""", ("Jaguuular1", "BRONZE", "V", "11"))

