from abc import ABC, abstractmethod
from src.domain.entity.blog_post import BlogPost
from typing import List
import uuid


class BlogPostPort(ABC):
    @abstractmethod
    async def create(self, blog_post: BlogPost) -> BlogPost:
        pass

    @abstractmethod
    async def find_by_id(self, id: int) -> BlogPost:
        pass

    @abstractmethod
    async def find_all_by_user_id(self, user_id: uuid.UUID) -> List[BlogPost]:
        pass

    @abstractmethod
    async def update(self, blog_post: BlogPost) -> BlogPost:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass
