from apis import ozon_parser
import time
from config import updating_time
import aiosqlite
import asyncio

class points_database:
    def __init__(self):
        self.db = None

    async def connect(self, folder='database/'):
        self.db = await aiosqlite.connect(f'{folder}db.db')

    async def check_point_by_address(self, address):
        cursor = await self.db.execute("SELECT id FROM points WHERE address == ?", (address, ))
        return await cursor.fetchone() is not None

    async def check_point_by_url(self, url):
        cursor = await self.db.execute('SELECT id FROM points WHERE url = ?', (url, ))
        return await cursor.fetchone() is not None

    async def add_point_ozon(self, url, wage, admin):
        if not await self.check_point_by_url(url):
            current_time = time.time()
            address, grade = await ozon_parser.parse_url(url)
            type = 'OZON'
            await self.db.execute('INSERT INTO points (created_at, updated_at, grade, url, address, type, wage, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (current_time, current_time, grade, url, address, type, wage, admin))
            await self.db.commit()
            return 'success'
        return 'already exists'

    async def add_point_wildberries(self, address, grade, wage, admin):
        if not await self.check_point_by_address(address):
            current_time = time.time()
            type = 'WILDBERRIES'
            await self.db.execute('INSERT INTO points (created_at, updated_at, grade, url, address, type, wage, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (current_time, current_time, grade, None, address, type, wage, admin))
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

class admins_database:
    def __init__(self):
        self.db = None

    async def connect(self, folder='database/'):
        self.db = await aiosqlite.connect(f'{folder}db.db')

    async def check_admin_by_id(self, admin_id):
        cursor = await self.db.execute('SELECT id FROM admins WHERE id = ?', (admin_id,))
        return await cursor.fetchone() is not None

    async def check_admin_by_login(self, login):
        cursor = await self.db.execute('SELECT id FROM admins WHERE login = ?', (login,))
        return await cursor.fetchone() is not None

    async def get_admin_data_by_id(self, admin_id):
        cursor = await self.db.execute('SELECT * FROM admins WHERE id = ?', (admin_id, ))
        data = await cursor.fetchone()
        return {'id': data[0], 'login': data[1], 'password': data[2]}

    async def get_admin_data_by_login(self, login):
        cursor = await self.db.execute('SELECT * FROM admins WHERE login = ?', (login,))
        data = await cursor.fetchone()
        return {'id': data[0], 'login': data[1], 'password': data[2]}

    async def add_admin(self, login, password):
        await self.db.execute('INSERT INTO admins (login, password) VALUES (?, ?)', (login, password))
        await self.db.commit()

    async def get_points(self, login, database):
        cursor = await database.execute('SELECT * FROM points WHERE admin = ?', (login, ))
        data = await cursor.fetchall()
        result = []
        for point in data:
            result.append({"id": point[0], "created_at": point[1], "updated_at": point[2], "grade": point[3], "url": point[4], "address": point[5], "type": point[6], "admin": point[7]})
        return result


async def main():
    adb = admins_database()
    await adb.connect('')
    await adb.add_admin('vasa', 'tupoy')
    print(await adb.check_admin_by_login('vasa'))

if __name__ == '__main__':
    asyncio.run(main())