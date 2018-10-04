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
    

    def test_get_menu(self):
        result = self.client().get('/api/v2/menu')
        self.assertEqual(result.status_code, 200)
        resp = json.loads(result.data.decode())
        self.assertIn('menu_list', resp)
        self.assertTrue(resp["menu_list"])

