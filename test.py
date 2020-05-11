import unittest
from app import app
import config

app.config.from_object('config.TestingConfig')


class TestGraf(unittest.TestCase):
    def setUp(self):
        """Set up app for testing"""
        self.app_test = app.test_client()

    def test_http_status(self):
        """Test if http status is 200"""
        res = self.app_test.get('/graf')
        self.assertEqual(res.status_code, 200)

    def test_mime_type(self):
        """Test if plot mime type is 'image/png'"""
        res = self.app_test.get('/plot.png')
        self.assertEqual(res.mimetype, 'image/png')


if __name__ == '__main__':
    unittest.main()
