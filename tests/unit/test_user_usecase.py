import unittest
from unittest.mock import Mock, MagicMock
from src.domain.entity.user import User
from src.app.usecase.user_usecase import UserUsecase

class TestUserUsecase(unittest.TestCase):

    def setUp(self):
        self.user_repository = Mock()
        self.user_usecase = UserUsecase(self.user_repository)

    def test_create_user(self):
        name = "Test User"
        email = "test@example.com"
        password = "password"

        self.user_repository.get_user_by_email.return_value = None
        self.user_repository.create_user.return_value = User(name, email, password)

        user = self.user_usecase.create_user(name, email, password)

        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_get_user_by_email(self):
        email = "test@example.com"
        self.user_repository.get_user_by_email.return_value = User("Test User", email, "password")

        user = self.user_usecase.get_user_by_email(email)

        self.assertEqual(user.email, email)

    def test_get_user_by_id(self):
        user_test = self.user_repository.get_user_by_id.return_value = User("Test User", "test@example.com", "password")

        user = self.user_usecase.get_user_by_id(user_test.id)

        self.assertEqual(user.id, user_test.id)

    def test_update_user(self):
        user_id = 1
        name = "Updated User"
        email = "updated@example.com"
        password = "updated_password"

        self.user_repository.update_user.return_value = User(name, email, password)

        user = self.user_usecase.update_user(user_id, name, email, password)

        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        

    def test_delete_user(self):
        user_id = 1

        self.user_usecase.delete_user(user_id)

        self.user_repository.delete_user.assert_called_once_with(user_id)
        
    def test_create_user_with_existing_email(self):
        email = "test@test.com"
        self.user_repository.get_user_by_email.return_value = User("Test User", email, "password")
        
        with self.assertRaises(ValueError):
            self.user_usecase.create_user("Test User", email, "password")
            
            
        

if __name__ == '__main__':
    unittest.main()