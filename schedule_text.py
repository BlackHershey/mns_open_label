from datetime import datetime, timedelta, timezone
from redis import Redis
from twilio.rest import Client
from rq_scheduler import Scheduler

import mns_open_label

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

with open('/home/numbers.txt') as f:
    numbers = f.readlines()
    numbers = [num.rstrip() for num in numbers]


d1 = datetime.strptime(str(datetime.now().date())+' 2:00 PM', '%Y-%m-%d %I:%M %p')
d2 = datetime.strptime(str(datetime.now().date() + timedelta(days=1)) +' 2:00 AM', '%Y-%m-%d %I:%M %p')

for num in numbers:
    scheduled_time = mns_open_label.generate_time(d1, d2)
    print(f'Texted {num} at {scheduled_time}')
    if scheduled_time:
        scheduler.enqueue_at(scheduled_time, mns_open_label.send_text, str(num))
