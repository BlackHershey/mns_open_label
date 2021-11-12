from datetime import datetime, timedelta, timezone
from redis import Redis
from twilio.rest import Client
from rq_scheduler import Scheduler
import pandas as pd

import mns_open_label

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

contact = pd.read_csv('/home/contact_info.csv')

d1 = datetime.strptime(str(datetime.now().date())+' 2:00 PM', '%Y-%m-%d %I:%M %p')
d2 = datetime.strptime(str(datetime.now().date() + timedelta(days=1)) +' 2:00 AM', '%Y-%m-%d %I:%M %p')

for index, row in contact.iterrows():
    num = str(row['Number'])
    on_link = row['On']
    off_link = row['Off']
    scheduled_time = mns_open_label.generate_time(d1, d2)
    print(f'Texted {num} at {scheduled_time}')
    if scheduled_time:
        scheduler.enqueue_at(scheduled_time, mns_open_label.send_text, num, on_link, off_link)
