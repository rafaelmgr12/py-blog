import datetime
from typing import List, Optional
import uuid
import re

from domain.entity.blog_post import BlogPost


class User:

    __id: uuid.UUID
    __name: str
    __email: str
    __password: str
    __created_at: datetime
    __updated_at: datetime
    __blog_posts: List[BlogPost]

    def __init__(self, name: str, email: str, password: str, blog_post: Optional[List[BlogPost]]=[]) -> None:
        self.__id = uuid.uuid4()
        self.__name = name
        self.__email = email
        self.__password = password
        self.__created_at = datetime.datetime.now()
        self.__updated_at = datetime.datetime.now()
        self.__blog_posts = blog_post
        
        
        self._validate()

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def _validate(self) -> None:
        if not self.__name:
            raise ValueError("Name is required")
        if not self.__email and self.validate_email(self.__email):
            raise ValueError("Email is required")
        if not self.__password:
            raise ValueError("Password is required")

    def _validate_email(self, email) -> None:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email")
