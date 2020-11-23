import configparser
from binance.client import Client

class ClientBot():
    def __init__(self, key_path):
        self.key_path = key_path

    def get_bot(self):
        config = configparser.RawConfigParser()
        config_path = self.key_path
        config.read(config_path)

        api_key = config.get('binance-keys', 'api_key')
        secret_key = config.get('binance-keys', 'secret_key')

        client = Client(api_key=api_key, api_secret=secret_key)
        return client
