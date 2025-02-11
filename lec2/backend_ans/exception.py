from fastapi import HTTPException

TRICK_ALREADY_EXIST = HTTPException(
    status_code=400, 
    detail="Trick already exists"
)
TRICK_NOT_FOUND = HTTPException(
    status_code=404, 
    detail="Trick not found"
)