import sqlalchemy
from src.domain.entity.user import User
from src.domain.ports.user import UserPort


class UserUsecase:

    def __init__(self, user_repository: UserPort):
        self.user_repository = user_repository

    async def create_user(self, name: str, email: str, password: str) -> User:
        user = User(name, email, password)
        user.hash_password()

        if await self.user_repository.find_by_email(email):
            raise ValueError("Email already exists")

        try:
            await self.user_repository.create(user)
        except Exception as e:
            raise str(e)

        return user

    async def get_user_by_email(self, email: str) -> User | None:
        try:
            return await self.user_repository.find_by_email(email)
        except Exception as e:
            raise e
        
    async def get_user_by_id(self, user_id: int) -> User | None:
        try:
            return await self.user_repository.find_by_id(user_id)
        except Exception as e:
            raise e
        
        
    async def update_user(self, user_id: int, name: str, email: str, password: str) -> User:
        user = User(name, email, password)
        user.hash_password()

        try:
            await self.user_repository.update(user_id, user)
        except Exception as e:
            raise e

        return user
    
    async def delete_user(self, user_id: int) -> None:
        try:
            await self.user_repository.delete(user_id)
        except Exception as e:
            raise e