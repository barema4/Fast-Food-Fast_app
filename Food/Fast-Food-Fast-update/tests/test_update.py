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
        


    def test_update_status(self):
        results = self.client().put('/api/v2/order/2', content_type='application/json',
                                    data=json.dumps({"status": "complete"}))
        self.assertEqual(results.status_code, 200)








