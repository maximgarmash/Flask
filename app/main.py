from flask import Flask
import requests
import json
import constants


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Test flask app<h1>'


# 1. Прием сообщений
# 2. Отслыка сообщений

URL = constants.url + constants.token


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
    url = URL + 'getUpdates'
    res = requests.get(url)
    return res.json()


def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def main():
    # res = requests.get(URL + 'getMe')
    # write_json(res.json())
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    send_message(chat_id)


if __name__ == "__main__":
    main()
