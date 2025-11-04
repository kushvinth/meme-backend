from pydantic import BaseModel, Field
from datetime import datetime


class Post(BaseModel):
    id: int
    title: str
    description: str
    # a timestamp is set automatically when one isn't provided.
    timestamp: datetime = Field(default_factory=datetime.utcnow)