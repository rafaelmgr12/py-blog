import unittest
from src.domain.entity.blog_post import BlogPost
import uuid


class TestBlogPost(unittest.TestCase):
    
    def setUp(self) -> None:
        self.title = "Test Title"
        self.content = "Test Content"
        self.author_id = uuid.uuid4()
        self.blog_post = BlogPost(self.title, self.content)
        
    
    def test_init(self):
        self.assertEqual(self.blog_post.title, self.title)
        self.assertEqual(self.blog_post.content, self.content)
        self.assertIsInstance(self.blog_post.id, uuid.UUID)
        
    def test_validate(self):
        with self.assertRaises(ValueError):
            BlogPost("", self.content)
        with self.assertRaises(ValueError):
            BlogPost(self.title, "")

            

if __name__ == '__main__':
    unittest.main()