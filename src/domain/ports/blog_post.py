from abc import ABC, abstractmethod
from src.domain.entity.blog_post import BlogPost
from typing import List


class BlogPostPort(ABC):
    
    @abstractmethod
    def create(self, blog_post: BlogPost) -> BlogPost:
        pass
    
    @abstractmethod
    def find_by_id(self, id: int) -> BlogPost:
        pass
    
    @abstractmethod
    def find_all_by_user_id(self) -> List[BlogPost]:
        pass
    
    @abstractmethod
    def update(self, blog_post: BlogPost) -> BlogPost:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass