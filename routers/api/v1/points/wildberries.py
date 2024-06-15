from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index_page():
    return {"status": True, "api": "Success"}