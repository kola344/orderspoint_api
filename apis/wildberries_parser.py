import aiohttp
import asyncio

async def get_response(session, url):
    while True:
        async with session.get(url, ssl=False) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(response.status)
                await asyncio.sleep(1)

async def get_by_ids(session, url, json_data):
    async with session.post(url, json=json_data, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {}

async def get_points(city):
    pickups_url = 'https://www.wildberries.ru/webapi/spa/modules/pickups'
    by_ids_url = 'https://www.wildberries.ru/webapi/poo/byids'

    async with aiohttp.ClientSession() as session:
        data = await get_response(session, pickups_url)
        pickups_info = {}

        for pickup in data['value']['pickups']:
            pickups_info[pickup['id']] = pickup

        json_data = list(pickups_info.keys())
        values = await get_by_ids(session, by_ids_url, json_data)
        values = values.get('value', {})

        for k, v in values.items():
            try:
                k_int = int(k)
                if k_int in pickups_info:
                    pickups_info[k_int].update(v)
            except ValueError:
                print(f"Unexpected key in response: {k}")

        result = []
        for key, value in pickups_info.items():
            if city in value.get('address', ''):
                result.append({'address': value.get('address', '-'), 'rate': value.get('rate', '-')})

    return result

async def main():
    points = await get_points('Саров')
    print(points)

if __name__ == '__main__':
    asyncio.run(main())