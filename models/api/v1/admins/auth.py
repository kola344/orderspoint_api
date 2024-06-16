from pydantic import BaseModel


class register(BaseModel):
    login: str
    password: str

class get_admin_by_id(BaseModel):
    admin_id: str

class get_admin_by_login(BaseModel):
    login: str