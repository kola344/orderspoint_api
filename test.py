import time
import requests


def get_response(url):
    response = requests.get(url)
    while response.status_code != 200:
        print(response.status_code)
        time.sleep(1)
        response = requests.get(url)

    return response


def get_by_ids(url, json_data):
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


if __name__ == '__main__':
    pickups_url = 'https://www.wildberries.ru/webapi/spa/modules/pickups'
    by_ids_url = 'https://www.wildberries.ru/webapi/poo/byids'

    data = get_response(pickups_url).json()
    pickups_info = {}

    for pickup in data['value']['pickups']:
        pickups_info[pickup['id']] = pickup

    json_data = list(pickups_info.keys())
    values = get_by_ids(by_ids_url, json_data).get('value', {})

    for k, v in values.items():
        k_int = int(k)
        print(k)
        if k_int in pickups_info:
            pickups_info[k_int].update(v)

    word_to_find = "Саров"
    for key, value in pickups_info.items():
        if word_to_find in value.get('address', ''):
            print('Адрес: ', value.get('address', '-'))
            print('Рейтинг: ', value.get('rate', '-'), '\n')