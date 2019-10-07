from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import requests
import json
import constants
import re

app = Flask(__name__)
sslify = SSLify(app)

# 1. Прием сообщений
# 2. Отслыка сообщений

URL = constants.url + constants.token


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# def get_updates():
#     url = URL + 'getUpdates'
#     res = requests.get(url)
#     return res.json()


def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    # write_json(r.json(), filename='price.json')
    return price


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        # write_json(r)
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        if parse_text(message):
            send_message(chat_id, get_price(parse_text(message)) + ' USD')
        return jsonify(r)
    return '<h1>Bot welcomes you<h1>'

def main():
    # res = requests.get(URL + 'getMe')
    # write_json(res.json())
    # r = get_updates()
    # chat_id = r['result'][-1]['message']['chat']['id']
    # send_message(chat_id)
    pass


if __name__ == "__main__":
    app.run()
    # main()

