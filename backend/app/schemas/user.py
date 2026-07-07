from pydantic import BaseModel
from datetime import datetime

class UserOut(BaseModel):
    id:int
    name:str
    role:str
    created_at :datetime

    model_config={"from_attributes" : True}
