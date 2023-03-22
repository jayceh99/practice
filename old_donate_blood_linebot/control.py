from apscheduler.schedulers.blocking import BlockingScheduler
import os
sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='sun', hour=8)
def scheduled_job():
    os.system('python3 /home/boss5510455/Blood_Notify/gcp_line_push_message.py')
sched.start()


