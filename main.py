import client_bot
import time
from datetime import datetime

cbot = client_bot.ClientBot('./key.cfg')
bot = cbot.get_bot()

start_of_day = datetime.now().strftime('%Y-%m-%d')
get_12oclock_timestamp = int(time.mktime(datetime.strptime(start_of_day, '%Y-%m-%d').timetuple()))
print(f'start_time: {get_12oclock_timestamp}')
info_btc_usdt = bot.get_klines(symbol='BTCUSDT', interval=bot.KLINE_INTERVAL_1DAY)
# info_btc_usdt = bot.get_historical_klines(symbol='BTCUSDT', interval=bot.KLINE_INTERVAL_1DAY, start_str='22 Nov 2020')



kline_open_time = info_btc_usdt[-1][0]
converted_open_time = datetime.fromtimestamp(kline_open_time/1000)

print(f'klines: {info_btc_usdt}')
print(info_btc_usdt[-1])
print(converted_open_time)
# print(start_of_day)

