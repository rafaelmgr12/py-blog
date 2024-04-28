from fastapi import HTTPException
from src.app.usecase.user_usecase import UserUsecase
from src.app.model.user import UserRequestCreate, UserResponse



class UserHandler:
    
    def __init__(self, user_usecase: UserUsecase) -> None:
        self.user_usecase = user_usecase
        
        
        
    def create_user(self, payload: UserRequestCreate) -> UserResponse:
        try:
            user = self.user_usecase.create_user(payload.name, payload.email, payload.password)
            return UserResponse(**user.dict())
        except (ValueError, Exception) as e:
            if e == ValueError("Email already exists"):
                raise HTTPException(status_code=404, detail="Email already exists")
            else:
                raise HTTPException(status_code=500, detail="Internal server error")
            
    
            