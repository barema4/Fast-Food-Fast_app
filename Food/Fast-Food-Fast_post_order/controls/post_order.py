
from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class NewOrder(MethodView):

    @jwt_required
    def post(self):

        if not request.json['order_name']:
            return jsonify({'message': " field should not be empty"}), 400

        if request.json["order_name"] == "":
            return jsonify({'message': 'place order'}), 400
        if not request.json['order_status']:
            return jsonify({'message': " field should not be empty"}), 400

        if request.json["order_status"] == "":
            return jsonify({'message': 'place order'}), 400

        user = get_jwt_identity()
        
        order = DatabaseConnection()
        new_order = order.insert_order(str(user[0]), request.json['order_name'],request.json['order_status'])

        if new_order == "order exits ":
            return jsonify({'message': "order not added"}), 401
        return jsonify({'message': new_order}), 201
