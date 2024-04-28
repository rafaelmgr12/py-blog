from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager


class DBConnect:
    def __init__(self, connection_string):
        self.engine = create_async_engine(
            connection_string,
            echo=True,  # Show SQL queries
            future=True  # Use the newest SQLAlchemy version
        )
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    @asynccontextmanager
    async def get_session(self):
        async_session = self.async_session()
        try:
            yield async_session
        except:
            await async_session.rollback()
            raise
        finally:
            await async_session.close()
