from pydantic import BaseModel, conint ,constr
from typing import Optional

class User(BaseModel):
    id: int
    name:str
    age:int
    email:str

user = User(id=1 , name="trim" , age = 17 , email="trimi@gmail.com")

print(user)


class User(BaseModel):
    id: int
    name: str
    age: Optional[int]
    email: Optional[str]


user1 = User(id=1, name="trim", age=17, )

print(user1)


class User(BaseModel):
    id: int
    name: str
    age: Optional[int]
    email: Optional[str]


user2 = User(id=1, name="trim", email="trimi@gmail.com")

print(user2)

class another_user(BaseModel):
    id:  conint(gt=0)
    name: constr(min_length=2 , max_length=50)

valid_user = another_user(id =1 , name = "John")
print(valid_user)

valid_user1 = another_user (id =0 , name= "j")
print(valid_user1)