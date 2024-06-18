from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Shelter, Animal

# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animal(cats=13, dogs=15)
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animal(cats=12, dogs=9)
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animal(cats=4, dogs=7)
    )
]



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers={"*"}
)

# get end points
@app.get("/shelters")
async def get_shelter_detail() -> list[Shelter]:
  return shelters


# post end points
@app.post("/shelter")
async def post_shelters(shelter: Shelter):
    shelters.append(shelter)
    return shelter

# put end points
@app.put("/shelter")
async def update_shelter(shelter_name: str, updated_shelter: Shelter):
    for i, shelter in enumerate(shelters):
        if shelter.name == shelter_name:
            shelters[i] = updated_shelter
            return updated_shelter
    shelters.append(updated_shelter)


# delete end points
@app.delete("/shelter/{shelter_name}")
async def delete_shelter(shelter_name: str):
    for i, shelter in enumerate(shelters):
        if shelter.name == shelter_name:
            deleted_shelter = shelters.pop(i)
            return deleted_shelter
    raise HTTPException(status_code=404, detail="Shelter not found")



      