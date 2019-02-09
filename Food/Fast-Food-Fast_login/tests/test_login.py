
import unittest
import json
from run import app
class UsersTest(unittest.TestCase):
    """
    Users Test Case
    """

    def setUp(self):
        """
        Test Setup
        """
        self.order = app
        self.client = self.order.test_client


    def test_user_login(self):
        """ User Login Tests """
        result = self.client().post('/api/v2/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="sam@gmail.com", password="12345678")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["message"])

    def test_user_login_with_invalid_password(self):

        result = self.client().post('/api/v2/auth/login', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(dict(email="sam@gmail.com", password="12345")))

        res = json.loads(result.data.decode("utf8"))
        self.assertIn('message', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["message"])

    def test_user_login_with_invalid_email(self):
        """ User Login Tests with invalid email """
        result = self.client().post('/api/v2/auth/login', headers={'Content-Type': 'application/json'},
                                    data=json.dumps(dict(email="samgmail.com", password="1234545677")))

        res = json.loads(result.data.decode("utf8"))
        self.assertIn('message', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["message"])

    def test_login(self):

        result = self.client().post('/api/v2/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="sam", password="12345678")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])
