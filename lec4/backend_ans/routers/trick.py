from fastapi import APIRouter

from exception import *
from schemas.trick import TrickCreate, TrickUpdate, Trick, TrickBase
router = APIRouter()



@router.get("/list")
async def get_tricks():
    trick_list = await Trick.find_all().project(TrickBase).to_list()
    return trick_list

@router.post("/add_trick")
async def add_trick(trick: TrickCreate):
    if await Trick.find_one(Trick.name == trick.name):
        raise TRICK_ALREADY_EXIST
    await Trick.insert_one(Trick(**(trick.model_dump())))
    return {"message": f"Trick '{trick.name}' added successfully"}

@router.patch("/update_trick")
async def update_trick(trick_update: TrickUpdate):
    trick = await Trick.find_one(Trick.name == trick_update.old_name)
    if trick is None:
        raise TRICK_NOT_FOUND
    await trick.set(trick_update.get_update_data())



    return {"message": f"Trick '{trick_update.old_name}' updated successfully"}
@router.delete("/delete_trick/")
async def delete_trick(trick_name: str):
    trick = await Trick.find_one(Trick.name == trick_name)
    if trick is None:
        raise TRICK_NOT_FOUND
    trick.delete()
    return {"message": f"Trick '{trick_name}' deleted successfully"}