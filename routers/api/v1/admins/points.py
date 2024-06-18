from fastapi import APIRouter
import db
from models.api.v1.admins import points

router = APIRouter()

@router.post('/get_points')
async def get_points_page(item: points.get_points):
    try:
        result = db.admin(item.login, db.point)
        return {'status': True, 'info': 'success', 'data': result}
    except Exception as e:
        return {"status": False, "info": f"err: {e}", 'data': []}

