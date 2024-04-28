import uuid
from abc import ABC, abstractmethod
from src.domain.entity.user import User

class UserPort(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def find_by_id(self, id: uuid.UUID) -> User:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, id: uuid.UUID) -> None:
        pass
