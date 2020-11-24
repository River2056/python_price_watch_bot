import client_bot
import time
from datetime import datetime

cbot = client_bot.ClientBot('../key.cfg')
bot = cbot.get_bot()

now = datetime.now()
now_timestamp = int(datetime.strptime(f'{now.year}-{now.month}-{24}', '%Y-%m-%d').timestamp())
# 1606148400000
# 1606003200000
# 1605974400
print(now_timestamp)

klines = bot.get_historical_klines(symbol='BTCUSDT', interval=bot.KLINE_INTERVAL_1MINUTE, start_str=str(now_timestamp))
print(f'started from {klines[1][0]}')
print(f'converted time: {datetime.fromtimestamp(klines[0][0]/1000)}')
print(f'ended in {klines[-1][0]}')
print(f'converted time: {datetime.fromtimestamp(klines[-1][0]/1000)}')