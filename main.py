from fastapi import FastAPI
from routers.api.v1.points import ozon, wildberries, yandex
import db

app = FastAPI()
app.include_router(ozon.router, prefix="/api/v1/points/ozon", tags=["ozon"])
app.include_router(wildberries.router, prefix="/api/v1/points/wildberries", tags=["wildberries"])
app.include_router(yandex.router, prefix="/api/v1/points/yandex", tags=["yandex"])

@app.get('/')
async def index_page():
    try:
        await db.initialize()
        return {"Status": True, "init": 'Success'}
    except Exception as e:
        return {"Status": False, "init": f"err: {e}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)