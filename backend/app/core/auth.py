from fastapi import HTTPException,Depends,Header
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

async def get_current_user(
        x_api_key :str |None =Header(default=None,alias="X-API-Key"),
        db :Session = Depends(get_db),
)->User:
    if x_api_key is None:
        raise HTTPException(status_code= 401,detail="invalid or missing API key")

    user = db.query(User).filter(User.api_key == x_api_key).first()
    if user is None:
        raise HTTPException(status_code= 401,detail="invalid or missing API key")
    return user
