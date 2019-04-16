

from tokens import cmc_token
import requests
import json
from flask import Flask
from flask import request
from flask import Response

token_telegram = '770447493:AAErrC8zYNNFWfJ51kd3h9kArJvZW3rx1_w'

app = Flask(__name__)

def write_json(data, filename='RespostaDo.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': crypto, 'convert': 'BRL'}
    header = {'X-CMC_PRO_API_KEY': cmc_token}

    responser = requests.get(url, headers=header, params=params).json()
    price = responser['data'][crypto]['quote']['BRL']['price']
    write_json(responser)
    return price

@app.route('/', methods= ['POST','GET'])

def index():
        if request.method == 'POST':
                msg = request.get_json()
                write_json(msg,'telegramjsson')
                return Response('ok',status=200)
        else:
                return '<h1> Bot Do Andrezin </h1>'





def main():
    print(get_cmc_data('BTC'))

   # f'https://api.telegram.org/bot770447493:AAErrC8zYNNFWfJ51kd3h9kArJvZW3rx1_w/sendMessage?chat_id=682423827&text=Eaemeubonissimo'

       # https://api.telegram.org/bot770447493:AAErrC8zYNNFWfJ51kd3h9kArJvZW3rx1_w/setWebhook?url=https://quibus.serveo.net/
if __name__ == '__main__':
    app.run(debug=True)
