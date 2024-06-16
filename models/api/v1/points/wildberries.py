from pydantic import BaseModel

class search_points_Item(BaseModel):
    query: str

class add_point_Item(BaseModel):
    address: str
    grade: str
    wage: str
    admin: str

class point_info_id_Item(BaseModel):
    point_id: int