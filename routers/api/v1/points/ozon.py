from fastapi import APIRouter
import db

router = APIRouter()

@router.get("/")
async def index_page():
    return {"status": True, "api": "success"}

@router.get("/add_point")
async def add_point_page(url: str, wage: str, admin: str):
    try:
        info = await db.point.add_point_ozon(url, wage, admin)
        return {"status": True, 'info': info}
    except Exception as e:
        return {"status": False, 'info': f'err: {e}'}

@router.get("/get_point_url")
async def point_info_url_page(url: str):
    '''ARGS: url'''
    try:
        data = await db.point.get_info_by_url(url)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}

@router.get('/get_point_id')
async def point_info_id_page(point_id: str):
    try:
        data = await db.point.get_info_by_id(point_id)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}


