from database import db
import asyncio

point = db.points_database()
admin = db.admins_database()
async def initialize():
    folder = 'database/'
    await point.connect(folder)
    await admin.connect(folder)
