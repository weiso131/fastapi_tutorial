from pydantic import BaseModel, Field
from typing import Optional
from beanie import Document

class TrickBase(BaseModel):
    name: str = Field(..., description="Name of the trick")
    difficulty: int = Field(..., description="Difficulty can be the humber from 1 to 10")
    video_link: Optional[str] = Field(None, description="The tutuiral video of the trick")
    tips: Optional[str] = Field(None, description="The text description of the trick tips")

class TrickCreate(TrickBase):
    pass

class Trick(TrickBase, Document):
    pass

class TrickUpdate(TrickBase):
    old_name: str = Field(..., description="Name of the trick")
    name: Optional[str] = Field(None, description="Name of the trick")
    difficulty: Optional[int] = Field(None, description="Difficulty can be the humber from 1 to 10")
    def get_update_data(self):
        update_data = self.model_dump(exclude={"old_name"}, exclude_none=True)
        return update_data


