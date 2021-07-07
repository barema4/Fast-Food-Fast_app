
from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class GetSpecificOrders(MethodView):
    @jwt_required
    def get(self,order_id):
        user = get_jwt_identity()
        user_type = user[4]
        if user_type != True:
            return jsonify(error='unauthorized access for admin'), 401


        order_item = DatabaseConnection()
        order_list =  order_item.get_one_order(order_id)
        if order_list == "No order available":
            return jsonify({"order": 'No specific order for this endpoint'}), 404
        return jsonify({"order_list":order_list})
    