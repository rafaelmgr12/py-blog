import datetime
import uuid
from typing import Optional


class BlogPost:
    __id: uuid.UUID
    __title: str
    __content: str
    user_id: uuid.UUID
    __created_at: datetime
    __updated_at: datetime

    def __init__(self, title: str, content: str, user_id: uuid.UUID, id: Optional[uuid.UUID] = None) -> str:
        if id:
            self.__id = id
        else:
            self.__id = uuid.uuid4()
        self.__title = title
        self.__content = content
        self.user_id = user_id
        self.__created_at = datetime.datetime.now()
        self.__updated_at = datetime.datetime.now()

        self._validate()

    def _validate(self):
        if not self.__title:
            raise ValueError("Title is required")
        if not self.__content:
            raise ValueError("Content is required")

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def user_id(self) -> uuid.UUID:
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id: uuid.UUID) -> None:
        self.__user_id = user_id

    @property
    def content(self) -> str:
        return self.__content
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at
    
    @property
    def updated_at(self) -> datetime:
        return self.__updated_at
