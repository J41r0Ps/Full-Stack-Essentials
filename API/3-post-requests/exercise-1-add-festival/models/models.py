from pydantic import BaseModel , Field
from datetime import date

class Festival(BaseModel):
    name : str = Field(...,min_length=3)
    location : str = Field(...,min_length=3)
    startDate : date
    endDate : date
    province : str = Field(...,min_length=3)
    comment: str = Field(default=None, max_length=250)