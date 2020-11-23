from datetime import datetime
import time

now = datetime.now().strftime('%Y-%m-%d')
print(now)

now_12oclock_timestamp = int(time.mktime(datetime.strptime(now, '%Y-%m-%d').timetuple()))
print(now_12oclock_timestamp)