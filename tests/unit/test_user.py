import unittest
import uuid
from src.domain.entity.user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "Test User"
        self.email = "testuser@test.com"
        self.password = "test123"
        self.user = User(self.name, self.email, self.password)

    def test_init(self):
        self.assertEqual(self.user.name, self.name)
        self.assertEqual(self.user.email, self.email)
        self.assertIsInstance(self.user.id, uuid.UUID)

    def test_validate(self):
        with self.assertRaises(ValueError):
            User("", self.email, self.password)
        with self.assertRaises(ValueError):
            User(self.name, "", self.password)
        with self.assertRaises(ValueError):
            User(self.name, self.email, "")


if __name__ == "__main__":
    unittest.main()
