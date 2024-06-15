import requests

API_KEY = '87dd0524-062c-4e56-b44d-3942721becedыгвщ фз'

def search_organizations(query):
    url = 'https://search-maps.yandex.ru/v1/'
    params = {
        'apikey': API_KEY,
        'text': query,
        'type': 'biz',
        'lang': 'ru_RU'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    query = 'кафе'
    result = search_organizations(query)
    # Обработка результата
    print(result)