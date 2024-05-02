from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.exc import SQLAlchemyError

from typing import List
import datetime

from src.domain.entity.blog_post import BlogPost
from src.domain.ports.blog_post import BlogPostPort
from src.infra.db.models.blog_post_model import BlogPostModel

import uuid


class SQLBlogPostRepository(BlogPostPort):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, blog_post: BlogPost) -> BlogPost:
        try:
            blog_post_model = BlogPostModel.from_domain(blog_post)
            self.session.add(blog_post_model)
            await self.session.commit()
            return blog_post_model.to_domain()
        except (SQLAlchemyError, Exception) as e:
            await self.session.rollback()
            raise e

    async def find_by_id(self, id: uuid.UUID) -> BlogPost:
        try:
            result = await self.session.execute(
                select(BlogPostModel).where(BlogPostModel.id == id)
            )
            blog_post_model = result.scalars().first()
            return blog_post_model.to_domain() if blog_post_model else None
        except (SQLAlchemyError, Exception) as e:
            raise e

    async def find_all_by_user_id(self, user_id: uuid.UUID) -> List[BlogPost]:
        try:
            result = await self.session.execute(
                select(BlogPostModel).where(BlogPostModel.user_id == user_id)
            )
            return [blog_post.to_domain() for blog_post in result.scalars().all()]
        except (SQLAlchemyError, Exception) as e:
            raise e

    async def update(self, blog_post: BlogPost) -> BlogPost:
        try:
            await self.session.execute(
                update(BlogPostModel)
                .where(BlogPostModel.id == blog_post.id)
                .values(
                    title=blog_post.title,
                    content=blog_post.content,
                    updated_at=datetime.datetime.now(),
                )
            )
            await self.session.commit()
            return blog_post
        except (SQLAlchemyError, Exception) as e:
            await self.session.rollback()

            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            await self.session.execute(
                delete(BlogPostModel).where(BlogPostModel.id == id)
            )
            await self.session.commit()
        except (SQLAlchemyError, Exception) as e:
            await self.session.rollback()
            raise e
