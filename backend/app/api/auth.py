from fastapi import APIRouter,Depends
from app.core.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserOut

router = APIRouter(prefix="/auth",tags=["auth"])

@router.get("/me",response_model =UserOut)
def  read_current_user(
    current_user : User=Depends(get_current_user),
)-> UserOut:
    return UserOut.model_validate(current_user)
