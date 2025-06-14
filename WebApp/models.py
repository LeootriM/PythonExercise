from pydantic import BaseModel
from typing import  List , Optional

class Developer(BaseModel):
    name:str
    experienceL: Optional[int] = None

class Project(BaseModel):
    title: str
    description: Optional[str] = None
    language: Optional[List[str]] = None
    lead_developer: Developer