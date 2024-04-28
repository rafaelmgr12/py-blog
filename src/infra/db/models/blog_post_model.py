from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import datetime
from src.domain.entity.blog_post import BlogPost
from src.infra.db.models.user_model import Base



class BlogPostModel(Base):
    __tablename__ = 'blog_posts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    @staticmethod
    def from_domain(blog_post: BlogPost) -> 'BlogPostModel':
        return BlogPostModel(
            id=blog_post.id,
            title=blog_post.title,
            content=blog_post.content,
            author_id=blog_post.author_id,
            created_at=blog_post.created_at,
            updated_at=blog_post.updated_at
        )

    def to_domain(self) -> BlogPost:
        return BlogPost(
            id=self.id,
            title=self.title,
            content=self.content,
            author_id=self.author_id
        )