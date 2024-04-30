from fastapi.testclient import TestClient
from main import create_app
import asyncio
import unittest

from dotenv import load_dotenv
import os

load_dotenv()

class TestUserIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(asyncio.run(create_app(os.getenv("POSTGRES_URL"), 8000, "localhost")))

    def test_create_user(self):
        payload = {
            "name": "New User",
            "email": "newuser@example.com",
            "password": "newpassword123"
        }
        response = self.client.post("/user", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

if __name__ == '__main__':
    unittest.main()