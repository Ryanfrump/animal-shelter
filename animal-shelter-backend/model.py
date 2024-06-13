from pydantic import BaseModel

class Shelter(BaseModel):
  name: str
  address: str
  animals: list["Animal"]


class Animal(BaseModel):
  cats: int
  dogs: int