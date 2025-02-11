from fastapi import APIRouter

from exception import *
from schemas.trick import TrickCreate, TrickUpdate
router = APIRouter()

trick_list = []


def __find_trick(trick_name: str):
    for trick in trick_list:
        if trick.name == trick_name:
            return trick
    return None

@router.get("/list")
def get_tricks():
    return trick_list

@router.post("/add_trick")
def add_trick(trick: TrickCreate):
    if trick in trick_list:
        raise TRICK_ALREADY_EXIST
    trick_list.append(trick)
    return {"message": f"Trick '{trick.name}' added successfully"}

@router.patch("/update_trick")
def update_trick(trick_update: TrickUpdate):
    trick = __find_trick(trick_update.old_name)
    if trick is None:
        raise TRICK_NOT_FOUND
    for key, value in trick_update.get_update_data().items():
        setattr(trick, key, value)


    return {"message": f"Trick '{trick_update.old_name}' updated successfully"}
@router.delete("/delete_trick/")
def delete_trick(trick_name: str):
    trick = __find_trick(trick_name)
    if trick is None:
        raise TRICK_NOT_FOUND
    trick_list.remove(trick)
    return {"message": f"Trick '{trick_name}' deleted successfully"}