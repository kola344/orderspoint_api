from fastapi import APIRouter
from apis import ozon_parser
from models.api.v1.points import ozon
import db

router = APIRouter()

@router.get("/")
async def index_page():
    return {"status": True, "api": "success"}

@router.get("/add_point")
async def add_point_page(url: str):
    try:
        info = await db.ozon.add_point(url)
        return {"status": True, 'info': info}
    except Exception as e:
        return {"status": False, 'info': f'err: {e}'}

@router.get("/get_point_url")
async def point_info_url_page(url: str):
    '''ARGS: url'''
    try:
        data = await db.ozon.get_info_by_url(url)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}

@router.get('/get_point_id')
async def point_info_id_page(point_id: str):
    try:
        data = await db.ozon.get_info_by_id(point_id)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}


