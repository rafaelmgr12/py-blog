import uuid

from src.domain.entity.blog_post import BlogPost
from src.domain.ports.blog_post import BlogPostPort
from src.domain.ports.user import UserPort


class BlogPostUseCase:

    def __init__(self, blog_post_repository: BlogPostPort, user_repository: UserPort)-> BlogPost:
        self.blog_post_repository = blog_post_repository
        self.user_repository = user_repository
        

    def create_blog_post(self, title: str, content: str, user_id: str)-> BlogPost:
        user_id_uuid = uuid.UUID(user_id)
        blog_post = BlogPost(title, content, user_id_uuid)
        
        user = self.user_repository.get_user_by_id(user_id_uuid)
        if not user:
            raise ValueError("User not found")
        
        try:
            return self.blog_post_repository.create_blog_post(blog_post)
        except Exception as e:
            raise e
        
        
    def get_blog_post_by_id(self, blog_post_id: str)-> BlogPost | None:
        blog_post_id_uuid = uuid.UUID(blog_post_id)
        try:
            return self.blog_post_repository.get_blog_post_by_id(blog_post_id_uuid)
        except Exception as e:
            raise e
        