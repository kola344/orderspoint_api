from fastapi import APIRouter
from apis import wildberries_parser
import db
from models.api.v1.points import wildberries

router = APIRouter()

@router.get("/")
async def index_page():
    return {"status": True, "api": "success"}

@router.post('/search_points')
async def search_points_page(item: wildberries.search_points_Item):
    try:
        info = await wildberries_parser.get_points(item.query)
        return {"status": True, 'info': info}
    except Exception as e:
        return {"status": False, 'info': f'err: {e}'}

@router.post("/add_point")
async def add_point_page(item: wildberries.add_point_Item):
    try:
        info = await db.point.add_point_wilberries(item.address, item.grade, item.wage, item.admin)
        return {"status": True, 'info': info}
    except Exception as e:
        return {"status": False, 'info': f'err: {e}'}

@router.post('/get_point_id')
async def point_info_id_page(item: wildberries.point_info_id_Item):
    try:
        data = await db.point.get_info_by_id(item.point_id)
        return {'status': True, 'info': 'success', 'data': data}
    except Exception as e:
        return {'status': False, 'info': f'err: {e}', 'data': {}}


