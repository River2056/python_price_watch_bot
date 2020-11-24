from datetime import datetime
from datetime import timedelta
import time

now = datetime.now()
print(f'now: {now}')
now_before_24hr = now - timedelta(hours=24)
print(f'24 hours ago: {now_before_24hr}')