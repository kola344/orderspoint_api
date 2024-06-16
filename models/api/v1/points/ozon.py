from pydantic import BaseModel

class add_point_Item(BaseModel):
    url: str
    wage: str
    admin: str

class point_info_url_Item(BaseModel):
    url: str

class point_info_id_Item(BaseModel):
    point_id: int