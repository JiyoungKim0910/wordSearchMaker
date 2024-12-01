from pydantic import BaseModel
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class GameCreate(BaseModel):
    title: str
    description: str
    grid_size: int
    words: List[str]