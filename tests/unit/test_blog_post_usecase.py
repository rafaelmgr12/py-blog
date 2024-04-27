import unittest
import uuid

from unittest.mock import Mock, MagicMock
from src.domain.entity.blog_post import BlogPost
from src.app.usecase.blog_post_usecase import BlogPostUseCase


class TestBlogPostUseCase(unittest.TestCase):

    def setUp(self):
        self.blog_post_repository = Mock()
        self.user_repository = Mock()
        self.blog_post_usecase = BlogPostUseCase(self.blog_post_repository, self.user_repository)

    def test_delete_blog_post_not_found(self):
        blog_post_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())

        self.blog_post_repository.get_blog_post_by_id.return_value = None

        with self.assertRaises(ValueError):
            self.blog_post_usecase.delete_blog_post(blog_post_id, user_id)

    def test_delete_blog_post_not_authorized(self):
        blog_post_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        other_user_id = str(uuid.uuid4())

        self.blog_post_repository.get_blog_post_by_id.return_value = BlogPost("Test Title", "Test Content", uuid.UUID(other_user_id))

        
        
        with self.assertRaises(ValueError):
            self.blog_post_usecase.delete_blog_post(blog_post_id, user_id)

    def test_delete_blog_post_success(self):
        blog_post_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())

        self.blog_post_repository.get_blog_post_by_id.return_value = BlogPost("Test Title", "Test Content", uuid.UUID(user_id))
        
        try:
            self.blog_post_usecase.delete_blog_post(blog_post_id, user_id)
        except Exception as e:
            self.fail(e)
            

if __name__ == '__main__':
    unittest.main()