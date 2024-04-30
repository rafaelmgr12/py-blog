from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.exc import SQLAlchemyError


import datetime

from src.domain.entity.user import User
from src.domain.ports.user import UserPort
from src.infra.db.models.user_model import UserModel

import uuid


class SQLUserRepository(UserPort):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> User:
        try:
            user_model = UserModel.from_domain(user)
            self.session.add(user_model)
            await self.session.commit()
            return user_model.to_domain()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e

    async def find_by_email(self, email: str) -> User:
        try:
            result = await self.session.execute(
                select(UserModel).where(UserModel.email == email)
            )
            user_model = result.scalars().first()
            return user_model.to_domain() if user_model else None
        except SQLAlchemyError as e:
            raise e

    async def find_by_id(self, id: uuid.UUID) -> User:
        try:
            result = await self.session.execute(
                select(UserModel).where(UserModel.id == id)
            )
            user_model = result.scalars().first()
            return user_model.to_domain() if user_model else None
        except SQLAlchemyError as e:
            raise e

    async def update(self, user: User) -> User:
        try:
            await self.session.execute(
                update(UserModel)
                .where(UserModel.id == user.id)
                .values(
                    name=user.name,
                    email=user.email,
                    password=user.hashed_password,
                    updated_at=datetime.datetime.now(),
                )
            )
            await self.session.commit()
            return user
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            await self.session.execute(delete(UserModel).where(UserModel.id == id))
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e
