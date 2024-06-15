from apis import ozon_parser
import time
from config import updating_time
import aiosqlite
import asyncio

class ozon_database:
    def __init__(self):
        self.db = None

    async def connect(self, folder='database/'):
        self.db = await aiosqlite.connect(f'{folder}db.db')

    async def check_point_by_url(self, url):
        cursor = await self.db.execute('SELECT id FROM points WHERE url = ?', (url, ))
        return await cursor.fetchone() is not None

    async def add_point(self, url):
        if not await self.check_point_by_url(url):
            current_time = time.time()
            address, grade = await ozon_parser.parse_url(url)
            type = 'OZON'
            await self.db.execute('INSERT INTO points (created_at, updated_at, grade, url, address, type) VALUES (?, ?, ?, ?, ?, ?)', (current_time, current_time, grade, url, address, type))
            await self.db.commit()
            return 'success'
        return 'already exists'

    async def get_info_by_url(self, url):
        if await self.check_point_by_url(url):
            cursor = await self.db.execute('SELECT * FROM points WHERE url = ?', (url, ))
            data = await cursor.fetchone()
            current_time = time.time()
            updated_at = data[2]
            if current_time - updated_at > updating_time:
                await self.db.execute('UPDATE points SET ? WHERE url = ?', (current_time, url))
                await self.db.commit()
                updated_at = current_time
            return {"id": data[0], "created_at": data[1], "updated_at": updated_at, "grade": data[3], "url": data[4], "address": data[5], "type": data[6]}

    async def check_point_by_id(self, point_id):
        cursor = await self.db.execute('SELECT id FROM points WHERE id = ?', (point_id,))
        return await cursor.fetchone() is not None

    async def get_info_by_id(self, point_id):
        if await self.check_point_by_id(point_id):
            cursor = await self.db.execute('SELECT * FROM points WHERE id = ?', (point_id,))
            data = await cursor.fetchone()
            current_time = time.time()
            updated_at = data[2]
            if current_time - updated_at > updating_time:
                await self.db.execute('UPDATE points SET ? WHERE id = ?', (current_time, point_id))
                await self.db.commit()
                updated_at = current_time
            return {"id": data[0], "created_at": data[1], "updated_at": updated_at, "grade": data[3], "url": data[4],
                    "address": data[5], "type": data[6]}


async def main():
    db = ozon_database()
    await db.connect('')
    await db.add_point('https://www.ozon.ru/geo/sarov/83676/')
    print(await db.check_point_by_url('https://www.ozon.ru/geo/sarov/83676/'))

if __name__ == '__main__':
    asyncio.run(main())