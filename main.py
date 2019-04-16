

from tokens import cmc_token
import requests
import json


def write_json(data, filename='RespostaDo.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': crypto, 'convert': 'BRL'}
    header = {'X-CMC_PRO_API_KEY': cmc_token}

    response = requests.get(url, headers=header, params=params).json()
    price = response['data'][crypto]['quote']['BRL']['price']
    write_json(response)
    return price


def main():
    print(get_cmc_data('BTC'))


if __name__ == '__main__':
    main()
