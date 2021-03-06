import json

from data.network.request import Request
from domain.crypto.coin import Coin


class CryptoRequest(Request):
    _ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/{coin_id}/?convert={conversion}"

    def __init__(self, coin_id, conversion):
        url = self._ENDPOINT.format(coin_id=coin_id, conversion=conversion)
        super(CryptoRequest, self).__init__(url)

    def execute(self, callback):
        response = self.get().response()
        if response:
            json_response = json.loads(self.response())[0]
            coin = Coin(json_response)
            callback(coin)
        else:
            callback(None)
