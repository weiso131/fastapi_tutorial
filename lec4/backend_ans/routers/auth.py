from fastapi import APIRouter
from .utils.jwt import *
import uuid
import bcrypt

from schemas.user import UserCreate, User

from exception import *

router = APIRouter()

@router.post('/register')
async def register(data: UserCreate):
    hashpw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    user_dict = data.model_dump()
    user_dict['password'] = hashpw.decode("utf-8")
    user_dict['uid'] = str(uuid.uuid4())

    if await User.find_one(User.email == data.email):
        return USER_ALREADY_EXISTS
    jwt_token = generate_tokens(user_dict)

    await User.insert_one(User(**user_dict))

    return jwt_token

@router.get('/login')
async def login(email: str, password: str):
    user = await User.find_one(User.email == email)
    if not user:
        return WRONG_EMAIL_OR_PASSWORD
    if not bcrypt.checkpw(password.encode(), user.password.encode("utf-8")):
        return WRONG_EMAIL_OR_PASSWORD
    
    user_dict = user.model_dump()
    user_dict.pop("id", None)

    return generate_tokens(user_dict)
