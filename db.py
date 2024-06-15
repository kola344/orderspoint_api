from database import db
import asyncio

ozon = db.ozon_database()
async def initialize():
    folder = 'database/'
    await ozon.connect(folder)
