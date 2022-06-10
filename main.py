import api
from time import sleep


def alert(coin: api.Coin, price_top: float, price_bottom: float):
    current_price = '{:,}'.format(coin.current_price)
    price_text = f'{coin.name}: {current_price}€'
    percent_change = f'[24h: {round(coin.price_change_24h, 2)}%]'

    if coin.current_price >= price_top:
        print(f'{price_text} {percent_change} --> TOP limit ({price_top}€).')
        # Insert code that you want to execute if coin reaches your TOP goal
        return

    if coin.current_price <= price_bottom:
        print(f'{price_text} {percent_change} --> BOTTOM limit ({price_bottom}€).')
        # Insert code that you want to execute if coin reaches your BOTTOM goal
        return

    print(price_text, f'{percent_change}')


def check_rates():
    coins = api.get_crypto_data()

    for coin in coins:
        if coin.symbol == 'xrp':
            alert(coin, price_top=0.3800, price_bottom=0.3500)

        if coin.symbol == 'btc':
            alert(coin, price_top=28_000, price_bottom=27_000)

        if coin.symbol == 'doge':
            alert(coin, price_top=0.1050, price_bottom=0.0750)


def main():
    i = 0
    while True:
        i += 1
        print(f'___ {i} ___')
        check_rates()
        sleep(60)  # Call the API every 30 seconds to check


if __name__ == '__main__':
    main()
