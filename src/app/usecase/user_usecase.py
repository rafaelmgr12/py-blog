from src.domain.entity.user import User
from src.domain.ports.user import UserPort


class UserUsecase:

    def __init__(self, user_repository: UserPort):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str, password: str) -> User:
        user = User(name, email, password)
        user.hash_password()

        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already exists")

        try:
            self.user_repository.create_user(user)
        except Exception as e:
            raise e

        return user

    def get_user_by_email(self, email: str) -> User | None:
        try:
            return self.user_repository.get_user_by_email(email)
        except Exception as e:
            raise e
        
    def get_user_by_id(self, user_id: int) -> User | None:
        try:
            return self.user_repository.get_user_by_id(user_id)
        except Exception as e:
            raise e
        
        
    def update_user(self, user_id: int, name: str, email: str, password: str) -> User:
        user = User(name, email, password)
        user.hash_password()

        try:
            self.user_repository.update_user(user_id, user)
        except Exception as e:
            raise e

        return user
    
    def delete_user(self, user_id: int) -> None:
        try:
            self.user_repository.delete_user(user_id)
        except Exception as e:
            raise e