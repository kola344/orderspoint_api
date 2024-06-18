from fastapi import APIRouter
import db
from models.api.v1.admins import auth

router = APIRouter()

@router.post('/register')
async def register_page(item: auth.register):
    try:
        await db.admin.add_admin(item.login, item.password)
        return {'status': True, 'info': "success"}
    except Exception as e:
        return {"status": False, "info": f"err: {e}"}

@router.post('/check_admin_by_id')
async def get_admin_by_id_page(item: auth.get_admin_by_id):
    try:
        check = await db.admin.check_admin_by_id(item.admin_id)
        return {'status': True, 'found': check, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}

@router.post('/check_admin_by_login')
async def get_admin_by_id_page(item: auth.get_admin_by_login):
    try:
        check = await db.admin.check_admin_by_login(item.login)
        return {'status': True, 'found': check, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}

@router.post('/get_admin_by_id')
async def get_admin_by_id_page(item: auth.get_admin_by_id):
    try:
        data = await db.admin.get_admin_data_by_id(item.admin_id)
        return {'status': True, 'data': data, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}

@router.post('/get_admin_by_login')
async def get_admin_by_id_page(item: auth.get_admin_by_login):
    try:
        data = await db.admin.get_admin_data_by_login(item.login)
        return {'status': True, 'data': data, 'info': 'success'}
    except Exception as e:
        return {'status': False, 'found': False, 'info': f'err: {e}'}
