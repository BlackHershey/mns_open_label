from datetime import datetime, timedelta, timezone
from twilio.rest import Client
import random

#Real
account_sid = 'AC1d2345f41654c309d21a2fe29b980973'
auth_token = '00f5137ee397f165d2bb716af2485070'

#Trial
#account_sid = 'AC6762650c8e7924d2c4b23fbbe5d9e59d'
#auth_token = '4e97f341f0fbf8abc3f75e66908a724e'

client = Client(account_sid, auth_token)

def generate_time(start, end):
    rand_time = start + timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
    return rand_time

def send_text(to, on, off):
    #Real
    client.messages.create(from_='+13148041421', to=to, body=f'MNS Study\nMy device is ON: {on}\nMy device is Off: {off}\nQuestions? 314-362-2083')
    #Fake
    #client.messages.create(from_='+13185268981', to=to, body='MNS Study: Please fill out the linked survey https://forms.gle/rYBJ55D2me8rxHqx5')