from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str
    user_id: Optional[int] = None

class Blog(BlogBase):
    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str 
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None

    class Config:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

###these are called base model
###they are used to dislplay the data in a specific format
