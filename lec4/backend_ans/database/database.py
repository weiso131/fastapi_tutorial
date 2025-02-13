from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from config import DC_NAME, URI
from schemas.trick import Trick
from schemas.user import User

tlsCAFileName = "mongodb-bundle.pem"
client = AsyncIOMotorClient(URI, tlsCAFile=tlsCAFileName)
db = client[DC_NAME]

async def init_database():
    await init_beanie(database=db, 
                      document_models=[
                          Trick,
                          User
                    ])
