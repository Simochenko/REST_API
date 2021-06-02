import pytest as pytest
import requests


class TestMarkets:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.response = requests.get("https://api-pub.bitfinex.com/v2/ticker/tBTCUSD")

    def test_code_is_200(self):
        assert self.response.status_code == 200, "status code is not 200"

    def test_has_10_values(self):
        assert len(self.response.json()) == 10, "response body contains not 10 values"

    def test_values_must_be_numbers(self):
        for value in self.response.json():
            assert isinstance(value, int) or isinstance(value, float), "value is not a number"
