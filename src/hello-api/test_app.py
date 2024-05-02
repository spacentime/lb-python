import unittest
from app import app

class TestHealthCheck(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_health_check(self):
        response = self.app.get('/health')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['message'], 'API is healthy')

if __name__ == '__main__':
    unittest.main()
