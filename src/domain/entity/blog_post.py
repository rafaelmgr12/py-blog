import datetime
import uuid


class BlogPost:
    __id: uuid.UUID
    __title: str
    __content: str
    __author_id: uuid.UUID
    __created_at: datetime
    __updated_at: datetime

    def __init__(self, title: str, content: str, author_id: uuid.UUID) -> str:
        self.__id = uuid.uuid4()
        self.__title = title
        self.__content = content
        self.__author_id = author_id
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
    def author_id(self) -> uuid.UUID:
        return self.__author_id

    @property
    def content(self) -> str:
        return self.__content
