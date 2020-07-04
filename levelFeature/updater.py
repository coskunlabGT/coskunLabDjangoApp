import requests
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler
import example_csv.csv


def read_csv(csv_file):

    with open(csv_file, "r") as file:
        for line in file:
            pass

    # Extracts data from most recent entry
    sr_num = int(line.split(',')[0])
    time = line.split(',')[1]
    level = int(line.split(',')[2])

    new_reading = {"sr_num": sr_num, "time": time, "reading_value": level}

    requests.delete(DELETE_READINGS)
    print('Deleted tasks')

    resp = requests.post(POST_LATEST, json=new_reading)
    print('Created task. ID: {}'.format(resp.json()["id"]))


scheduler = BackgroundScheduler()
scheduler.add_job(read_csv, CronTrigger.from_crontab('2 * * * *'), args=[example_csv])
scheduler.start()
