from fastapi import HTTPException

TRICK_ALREADY_EXIST = HTTPException(
    status_code=400, 
    detail="Trick already exists"
)
TRICK_NOT_FOUND = HTTPException(
    status_code=404, 
    detail="Trick not found"
)
USER_ALREADY_EXISTS = HTTPException(
    status_code=400,
    detail="The account is already exist"
)

WRONG_EMAIL_OR_PASSWORD = HTTPException(
    status_code=400,
    detail="wrong email or password"
)
TOKEN_EXPIRED = HTTPException(
    status_code=400, 
    detail="token expired"
)
TOKEN_INVALID = HTTPException(
    status_code=400, 
    detail="token invalid"
)
INSUFFICIENT_PERMISSIONS = HTTPException(
    status_code=400, 
    detail="insufficient permissions"
)