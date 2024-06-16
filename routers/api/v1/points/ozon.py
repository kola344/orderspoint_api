from fastapi import APIRouter
import db
from models.api.v1.points import ozon

router = APIRouter()

@router.get("/")
async def index_page():
    return {"status": True, "api": "success"}

@router.post("/add_point")
async def add_point_page(item: ozon.add_point_Item):
    try:
        info = await db.point.add_point_ozon(item.url, item.wage, item.admin)
        return {"status": True, 'info': info}
    except Exception as e:
        return {"status": False, 'info': f'err: {e}'}

@router.post("/get_point_url")
async def point_info_url_page(item: ozon.point_info_url_Item):
    '''ARGS: url'''
    try:
        data = await db.point.get_info_by_url(item.url)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}

@router.post('/get_point_id')
async def point_info_id_page(item: ozon.point_info_id_Item):
    try:
        data = await db.point.get_info_by_id(item.point_id)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}


