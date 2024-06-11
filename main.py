from fastapi import FastAPI
from routers.api.v1.points import ozon, wildberries, yandex

app = FastAPI()
app.include_router(ozon.router, prefix="/api/v1/points/ozon", tags=["ozon"])
app.include_router(wildberries.router, prefix="/api/v1/points/wildberries", tags=["wilberries"])
app.include_router(yandex.router, prefix="/api/v1/points/yandex", tags=["yandex"])

@app.get('/')
def index_page():
    return {"Status": True}