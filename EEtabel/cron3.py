from django_cron import cronScheduler, Job
from django_cron import cronScheduler as cron

from EEtabel import Summoners

class CheckMail(Job):

        # run every 300 seconds (5 minutes)
        run_every = 300

        def job(self):
                # This will be executed every 5 minutes
                check_feedback_mailbox()

cronScheduler.register(CheckMail)