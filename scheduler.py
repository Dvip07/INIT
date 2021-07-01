# schedule

import schedule
import time
from datetime import datetime
import random

def abd():
    now=datetime.now().time()
    print("Curret time :", now)
    a="abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwordlen=20
    passwd="".join(random.sample(a, passwordlen))
    print(passwd)

schedule.every().day.at("21:00").do(abd)
# schedule.every(10).seconds.do(abd)
while 1:
    schedule.run.pending()
    time.sleep(1)
