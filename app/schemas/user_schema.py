from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True # Changed from orm_mode


class UserLogin(BaseModel):
    username: str
    password: str