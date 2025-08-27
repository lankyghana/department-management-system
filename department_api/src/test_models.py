import unittest
from src.models.department import Department
from src.models.user import User

class TestDepartmentModel(unittest.TestCase):
    def test_to_dict(self):
        dept = Department(id=1, name='IT', description='Tech')
        self.assertEqual(dept.to_dict(), {'id': 1, 'name': 'IT', 'description': 'Tech'})

class TestUserModel(unittest.TestCase):
    def test_to_dict(self):
        user = User(id=1, username='admin', email='admin@example.com')
        self.assertEqual(user.to_dict(), {'id': 1, 'username': 'admin', 'email': 'admin@example.com'})

if __name__ == '__main__':
    unittest.main()
