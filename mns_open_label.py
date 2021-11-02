from datetime import datetime, timedelta, timezone
from twilio.rest import Client
import random

account_sid = 'AC1d2345f41654c309d21a2fe29b980973'
auth_token = '8c4f623f07a2fc394772a8678017993f'

client = Client(account_sid, auth_token)

def generate_time(start, end):
    rand_time = start + timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
    return rand_time

def send_text(to):
    client.messages.create(from_='+13148041421', to=to, body='MNS Study: Please fill out the linked survey https://forms.gle/rYBJ55D2me8rxHqx5')


