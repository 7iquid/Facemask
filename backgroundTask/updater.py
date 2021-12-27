from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api, dateChecker


def start():
	dateChecker()
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'cron', hour='8' ,timezone='Asia/Shanghai')
	scheduler.start()

