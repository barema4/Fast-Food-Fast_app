
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

    def test_post_item_on_menu_by_admin(self):
        result = self.client().post('/api/v2/menu', content_type="application/json", data=json.dumps(
            dict(item="matoke")))
        self.assertEqual(result.status_code, 401)
        resp = json.loads(result.data.decode())
        self.assertIn('msg', resp)
        self.assertTrue(resp["msg"])
