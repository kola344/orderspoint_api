from fastapi import APIRouter
import db

router = APIRouter()

@router.get('/register')
async def register_page(login: str, password: str):
    try:
        await db.admin.add_admin(login, password)
        return {'status': True, 'info': "success"}
    except Exception as e:
        return {"status": False, "info": f"err: {e}"}

@router.get('/get_admin_by_id')
async def get_admin_by_id_page(admin_id: str):
    try:
        check = await db.admin.check_admin_by_id(admin_id)
        return {'status': True, 'found': check, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}

@router.get('/get_admin_by_login')
async def get_admin_by_id_page(login: str):
    try:
        check = await db.admin.check_admin_by_login(login)
        return {'status': True, 'found': check, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}
