import uuid
from abc import ABC, abstractmethod
from src.domain.entity.user import User

class UserPort(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: uuid.UUID) -> None:
        pass
