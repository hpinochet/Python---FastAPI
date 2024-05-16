from pydantic import BaseModel
from typing import List, Optional

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas : int
    editorial: Optional[str]

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True
    pass

class ShowBlogTitle(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True
    pass

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None