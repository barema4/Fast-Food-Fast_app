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

    def test_user_creation(self):
        """ test user creation with invalid credentials """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="ken eth", email="sam @gmail.com",
                                                         password="23456")))
        res = json.loads(result.data.decode("utf8"))
        self.assertIn('message', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_user_creation_with_wrong_email(self):
        """ test user creation with already wrong email"""
        result = self.client().post('/api/v2/auth/signup',
                                   content_type="application/json",
                                   data=json.dumps(dict(user_name="keneth", email="sam gmail.com",
                                                        password="23456123")))
        res = json.loads(result.data.decode("utf8"))
        self.assertIn('email', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["email"])

    def test_user_creation_with_no_password(self):
        """ test user creation with no password"""
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="keneth", email="sam@gmail.com",
                                                         password="")))
        res = json.loads(result.data.decode("utf8"))
        self.assertIn('message', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])


    def test_user_creation_with_no_user_name(self):

        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", email="sam@gmail.com",
                                                         password="")))
        res = json.loads(result.data.decode("utf8"))
        self.assertIn('user_name', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["user_name"])


    def test_user_creation_with_empty_request(self):
        """ test user creation with empty request """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict()))
        res = json.loads(result.data.decode("utf8"))
        self.assertIn('message', res)
        self.assertIsInstance(res, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])
