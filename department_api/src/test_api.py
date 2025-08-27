import unittest
from src.main import app

class TestDepartmentAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_departments(self):
        response = self.client.get('/api/departments')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_department_missing_name(self):
        response = self.client.post('/api/departments', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
