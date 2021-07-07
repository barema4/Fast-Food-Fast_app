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

    def test_get_one_orders_by_admin(self):
        result = self.client().get('/api/v2/orders')
        self.assertEqual(result.status_code, 401)
        resp = json.loads(result.data.decode())
        self.assertIn('msg', resp)
        self.assertTrue(resp["msg"])
