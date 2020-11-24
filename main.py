import time
import client_bot
from datetime import datetime
from datetime import timedelta

cbot = client_bot.ClientBot('./key.cfg')
bot = cbot.get_bot()

'''
response example
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "17928899.62484339" // Ignore.
  ]
]
'''

def get_price_and_percentage_change(symbol, bot):
    now = datetime.now()
    now_timestamp = int(datetime.strptime(f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}', '%Y-%m-%d %H:%M:%S').timestamp())
    now_24hrs_ago = now - timedelta(hours=24)
    now_ago_timestamp = int(datetime.strptime(f'{now_24hrs_ago.year}-{now_24hrs_ago.month}-{now_24hrs_ago.day} {now_24hrs_ago.hour}:{now_24hrs_ago.minute}:{now_24hrs_ago.second}', '%Y-%m-%d %H:%M:%S').timestamp())
    klines = bot.get_historical_klines(symbol=symbol, interval=bot.KLINE_INTERVAL_1MINUTE, start_str=str(now_ago_timestamp), end_str=str(now_timestamp))
    # print(f'started from {klines[1][0]}')
    print(f'converted start time: {datetime.fromtimestamp(klines[0][0] / 1000)}')
    # print(f'ended in {klines[-1][0]}')
    print(f'converted end time: {datetime.fromtimestamp(klines[-1][0] / 1000)}')

    # count price change percentage
    percentage = ((float(klines[-1][4]) - float(klines[0][4])) / float(klines[0][4])) * 100
    print(f'{symbol} first close price: {klines[0][4]}')
    print(f'{symbol} latest close price: {klines[-1][4]}')
    print(f'{symbol} price changes: {percentage}')
    time.sleep(3)


get_price_and_percentage_change('BTCUSDT', bot)
get_price_and_percentage_change('ETHUSDT', bot)
get_price_and_percentage_change('BNBUSDT', bot)
get_price_and_percentage_change('XRPUSDT', bot)
get_price_and_percentage_change('BCHUSDT', bot)
get_price_and_percentage_change('LTCUSDT', bot)