    
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
            dict(item="matoke",price="3000/=")))
        self.assertEqual(result.status_code, 401)
        self.assertTrue(resp["msg"])

    def test_get_menu(self):
        result = self.client().get('/api/v2/menu')
        resp = json.loads(result.data.decode())
        self.assertIn('msg', resp)
        self.assertEqual(result.status_code, 200)
        resp = json.loads(result.data.decode())
        self.assertIn('menu_list', resp)
        self.assertTrue(resp["menu_list"])
