import requests
from dataclasses import dataclass


@dataclass(slots=True)
class Coin:
    symbol: str
    name: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float


# https://www.coingecko.com/en/api/documentation
def get_crypto_data() -> list[Coin]:
    base_url = 'https://api.coingecko.com/api/v3/coins/markets'
    payload = {'vs_currency': 'eur',
               'order': 'market_cap_desc'}

    data = requests.get(base_url, params=payload)
    json = data.json()

    # Create a list of coins and append it to our list
    coin_list = []
    for item in json:
        current = Coin(symbol=item['symbol'],
                       name=item['name'],
                       current_price=item['current_price'],
                       high_24h=item['high_24h'],
                       low_24h=item['low_24h'],
                       price_change_24h=item['price_change_percentage_24h'])

        coin_list.append(current)

    return coin_list


if __name__ == '__main__':
    for coin in get_crypto_data():
        print(coin)
