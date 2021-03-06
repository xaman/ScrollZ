import schedule

from data.network.crypto_request import CryptoRequest
from domain.crypto.conversion import Conversion
from provider import Provider


class CryptoProvider(Provider):
    _SCHEDULE_MINUTES = 5

    def __init__(self, coin_id, formatter, conversion=Conversion.EUR):
        super(CryptoProvider, self).__init__()
        self.coin_id = coin_id
        self.formatter = formatter
        self.conversion = conversion

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        request = CryptoRequest(self.coin_id, self.conversion)
        request.execute(self._on_result)

    def _on_result(self, data):
        self.data = data
        self.logger.debug(data)
