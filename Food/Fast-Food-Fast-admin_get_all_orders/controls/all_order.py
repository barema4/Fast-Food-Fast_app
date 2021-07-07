
from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class GetOrders(MethodView):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        user_type=user[4]
        print(user_type)
        if user_type != True:

            return jsonify(error='Unauthorized access for admin'), 401

        order_item = DatabaseConnection()
        order_list = order_item.all_orders()
        print(order_list)

        return jsonify({"order_list":order_list}),200
        
