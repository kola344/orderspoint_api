from config import yandex_maps_APIKEY
import requests

def get_city_coordinates(city_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }
    response = requests.get(url, params=params)
    print('\n\n\n\n\n\n\n\n\n\n')
    print(response.text)
    print('\n\n\n\n\n\n\n\n\n\n')
    data = response.json()

    if not data:
        raise ValueError(f"Не удалось найти координаты для города: {city_name}")

    city_data = data[0]
    return float(city_data["lat"]), float(city_data["lon"])


def get_yandex_maps_data(api_key, lat, lon, query):
    base_url = "https://search-maps.yandex.ru/v1/"
    bbox = f"{lon - 0.1},{lat - 0.1}~{lon + 0.1},{lat + 0.1}"  # Adjust the bounding box size as needed
    params = {
        "apikey": api_key,
        "text": query,
        "lang": "ru_RU",
        "type": "biz",
        "results": 100,
        "bbox": bbox
    }
    response = requests.get(base_url, params=params)
    return response.json()


def parse_pvz_data(data):
    pvz_list = []
    for feature in data.get("features", []):
        properties = feature.get("properties", {})
        company_meta_data = properties.get("CompanyMetaData", {})
        pvz_info = {
            "name": company_meta_data.get("name"),
            "address": company_meta_data.get("address"),
            "url": company_meta_data.get("url"),
            "phone": company_meta_data.get("Phones", [{}])[0].get("formatted"),
            "working_hours": company_meta_data.get("Hours", {}).get("text"),
            "categories": company_meta_data.get("Categories", [{}])[0].get("name")
        }
        pvz_list.append(pvz_info)
    return pvz_list


def search_object(city, query, lat = None, lon = None):
    api_key = yandex_maps_APIKEY

    if lat == None or lon == None:
        lat, lon = get_city_coordinates(city)
    data = get_yandex_maps_data(api_key, lat, lon, query)
    pvz_list = parse_pvz_data(data)

    return pvz_list

if __name__ == '__main__':
    city = 'Ворсма'
    query = 'ПВЗ Wildberries'
    for i in search_object(city, query):
        print(i)