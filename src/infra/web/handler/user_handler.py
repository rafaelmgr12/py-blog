from fastapi import HTTPException
from src.app.usecase.user_usecase import UserUsecase
from src.app.model.user import UserRequestCreate, UserResponse


class UserHandler:
    def __init__(self, user_usecase: UserUsecase) -> None:
        self.user_usecase = user_usecase

    async def create_user(self, payload: UserRequestCreate) -> UserResponse:
        try:
            user = await self.user_usecase.create_user(
                payload.name, payload.email, payload.password
            )
            return UserResponse(id=str(user.id), name=user.name, email=user.email)
        except ValueError as e:
            if str(e) == "Email already exists":
                raise HTTPException(status_code=400, detail="Email already exists")
            else:
                raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
