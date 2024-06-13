from pydantic import BaseModel

class Shelter(BaseModel):
  name: str
  address: str
  animals: "Animal"


class Animal(BaseModel):
  cats: int
  dogs: int