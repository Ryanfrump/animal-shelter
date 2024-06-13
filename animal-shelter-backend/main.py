from fastapi import FastAPI

from model import Shelter, Animal

# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
shelters: list[Shelter] = [
    {
        "name": "St. George Animal Shelter",
        "address": "605 Waterworks Dr, St. George, UT 84770",
        "animals": {
            "cats": 13,
            "dogs": 15,
        }
    },
    {
        "name": "St. George Paws",
        "address": "1125 W 1130 N, St. George, UT 84770",
        "animals": {
            "cats": 12,
            "dogs": 9,
        }
    },
    {
        "name": "Animal Rescue Team",
        "address": "1838 W 1020 N Ste. B, St. George, UT 84770",
        "animals": {
            "cats": 4,
            "dogs": 7,
        }
    }
]



app = FastAPI()



# get end points
@app.get("/shelter_name")
async def get_shelter_name():
  return [shelter["name"] for shelter in shelters]

@app.get("/shelter")
async def get_shelter_detail():
  return shelters

@app.get("/{shelter_name}/address")
async def get_shelter_address(shelter_name):
  for shelter in shelters:
    if shelter["name"] == shelter_name:
      return f"{shelter_name}'s address is {shelter["address"]}"

@app.get("/{shelter_name}/cats")
async def get_cats_by_shelter(shelter_name: str):
  for shelter in shelters:
    if shelter["name"] == shelter_name:
      return f"There are {shelter["animals"]["cats"]} cats in {shelter_name}"
  return {"message": "Shelter not found"}

@app.get("/{shelter_name}/dogs")
async def get_dogs_by_shelter(shelter_name: str):
  for shelter in shelters:
    if shelter["name"] == shelter_name:
      return f"There are {shelter["animals"]["dogs"]} dogs in {shelter_name}"
  return {"message": "Shelter not found"}


# post end points

# put end points

# delete end points



      